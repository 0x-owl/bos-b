# '''
# random investigator generator module.
# '''
from random import randint, choice, shuffle

from django.contrib.auth import get_user_model

from creator.models import (Investigator, Occupation, Skills)
from creator.helpers.model_helpers import roller_stats

from creator.helpers.random_name import random_names


User = get_user_model()


def amount(points_available: int, limit: int):
    """Generate an adequate random value for the points assignment."""
    limit = min(points_available, 91-limit)
    val = randint(1, limit)
    return val


def occ_point_assigner(max_points: int, skills: dict, inv: Investigator):
    """Assign points for the skills related to occupations."""
    # Assing profession points
    compulsory_skills = skills['skill_profession']
    skills_used = ['Credit Rating']
    inv.skills[comp_skill]['Credit Rating']['value'] = randint(
        inv.occupation.credit_rating_min,
        inv.occupation.credit_rating_max
    )
    inv.save()
    skills_used['Credit Rating'] = credit_rating

    val = (max_points // 2) // len(compulsory_skills)
    for comp_skill in compulsory_skills:
        inv.skills[comp_skill]['value'] = inv.skills[
            comp_skill]['default_value'] + val
        max_points -= val
        skills_used.append(comp_skill)
        inv.save()
    # TODO: mandatories base value covered now grab all by their
    # list respecting the limit
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
    skills = Skills.objects.filter(year=1920).first()['skills']
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
        "luck": roller_stats(3),
        "skills": skills
    }
    inv = Investigator(**attrs)
    inv.save()
    # Load derivative statuses
    inv.health = inv.max_health
    inv.sanity = inv.power
    inv.save()
    # Obtain skills and occupations related to the investigator occupation.
    if occ_skills:
        proff_points = inv.occupation_skill_points
        # Assign points to occupation skills

        skills_assigned = occ_point_assigner(
            proff_points, inv.occupation.skills, inv)

        skills_assigned = point_assigner(
            inv.free_skill_points, inv.skills, inv)
        for skill in skills_assigned:
            skills_assigned[skill].save()
    else:
        raise Exception(
            f"No occupation skills for occupation {inv.occupation}"
        )

    return inv.uuid
