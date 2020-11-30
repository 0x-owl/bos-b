# '''
# random investigator generator module.
# '''
from random import randint, choice, shuffle

from django.contrib.auth import get_user_model

from creator.models import (Investigator, Occupation, Skills)
from creator.helpers.model_helpers import attribute_roller, roller_stats

from creator.helpers.random_name import random_names


User = get_user_model()


def calc_proff_points(attribute: int, mod: int, inv: Investigator):
    """Calculate the amount of points that correspond to certain attribute"""
    inv_attrs = InvestigatorAttribute.objects.filter(
        attr=attribute,
        investigator=inv
    ).first()
    res = inv_attrs.value * mod
    return res


def load_investigator_attributes(inv: Investigator):
    """Seed an investigator with attributes."""
    # Obtain list of attibutes with their ids.
    attrs = Attribute.items()

    # Seed attributes
    for attr in attrs:
        inv_attr = InvestigatorAttribute(
            investigator=inv,
            attr=attr[1],
            value=attribute_roller(attr[1])
        )
        inv_attr.save()


def amount(points_available: int, limit: int):
    """Generate an adequate random value for the points assignment."""
    limit = min(points_available, 90-limit)
    val = randint(1, limit)
    return val


def occ_point_assigner(max_points: int, occ_skills: list, inv: Investigator):
    """Assign points for the skills related to occupations."""
    # Assing profession points
    compulsory_skills = [sk for sk in occ_skills if sk.category == '1']
    skills_used = {}
    # set credit rating as a separate skill
    credit_rating_skill = Skills.objects.filter(
        title="Credit Rating"
    )[0]
    cr_value = randint(
        inv.occupation.credit_rating_min,
        inv.occupation.credit_rating_max
    )
    credit_rating = InvestigatorSkills(
        investigator=inv,
        skill=credit_rating_skill,
        value=cr_value,
        category="1"
    )
    credit_rating.save()
    skills_used[credit_rating_skill.uuid] = credit_rating

    val = (max_points // 2) // len(compulsory_skills)
    for comp_skill in compulsory_skills: 
        record = InvestigatorSkills(
            investigator=inv,
            skill=comp_skill.skill,
            value=comp_skill.skill.default_value + val,
            category=comp_skill.category
        )
        max_points -= val
        skills_used[comp_skill.skill.uuid] = record

    occ_skills = list(occ_skills)
    shuffle(occ_skills)
    for occ_skill in occ_skills:
        # If not create a new record else update the new one.
        if max_points:
            if occ_skill.skill.uuid not in list(skills_used.keys()):
                # Remember not to surpass 99 limit
                val = amount(max_points, occ_skill.skill.default_value)
                record = InvestigatorSkills(
                    investigator=inv,
                    skill=occ_skill.skill,
                    value=occ_skill.skill.default_value + val,
                    category=occ_skill.category
                )
                max_points -= val
                skills_used[occ_skill.skill.uuid] = record

            else:
                record = skills_used[occ_skill.skill.uuid]
                # Remember not to surpass the 90 limit
                val = amount(max_points, record.value)
                if (record.value + val) < 90:
                    record.value += val
                    max_points -= val
        else:
            break
    return skills_used


def free_point_assigner(max_points: int, skills: list,
                        inv: Investigator, skills_assigned: dict):
    """Assign points to any skill."""
    skills_used = skills_assigned
    skills = list(skills)
    shuffle(skills)
    for skill in skills:
        if max_points:
            # If not create a new record else update the new one.
            if skill.uuid not in list(skills_used.keys()):
                # Remember not to surpass 99 limit
                val = amount(max_points, skill.default_value)
                record = InvestigatorSkills(
                    investigator=inv,
                    skill=skill,
                    value=skill.default_value + val,
                    category='4'
                )
                max_points -= val
                skills_used[skill.uuid] = record

            else:
                record = skills_used[skill.uuid]
                # Remember not to surpass the 90 limit
                val = amount(max_points, record.value)
                if (record.value + val) < 90:
                    record.value += val
                    max_points -= val
        else:
            break
    return skills_used

def random_inv():
    """Main wrapper."""
    # Pick a random occupation
    occ = Occupation.objects.get(pk=randint(1, 117))
    genders = [('M', 'male'), ('F', 'female')]
    gender_pick = choice(genders)
    name = random_names(gender_pick[1], "20'", 1, 1)
    attrs = {
        "user": User.objects.get(pk=1),
        "name": name,
        "player": f"{name} player",
        "sex": gender_pick[0],
        "residence": "Providence",
        "birthplace": "Misissippi",
        "age": randint(15, 90),
        "occupation": occ,
        "ideologies": "Atheist",
        "sanity": roller_stats(3),
        "luck": roller_stats(3)
    }
    inv = Investigator(**attrs)
    inv.save()
    load_investigator_attributes(inv)
    # Load derivative statuses
    inv.health = inv.max_health
    inv.sanity = inv.power.value
    inv.save()
    # Obtain skills and occupations related to the investigator occupation.
    occ_skills = OccupationSkills.objects.filter(occupation=inv.occupation)
    if occ_skills   :
        proff_points = inv.occupation_skill_points
        # Assign points to occupation skills
        skills_assigned = occ_point_assigner(
            proff_points, occ_skills, inv)
        free_skills = Skills.objects.all()
        skills_assigned = free_point_assigner(
            inv.free_skill_points, free_skills, inv, skills_assigned)
        for skill in skills_assigned:
            skills_assigned[skill].save()
    else:
        raise Exception(
            f"No occupation skills for occupation {inv.occupation}"
        )

    return inv.uuid
