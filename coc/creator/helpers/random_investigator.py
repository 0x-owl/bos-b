# '''
# random investigator generator module.
# '''
from random import randint, choice, shuffle

from django.contrib.auth import get_user_model

from creator.helpers.model_helpers import roller_stats
from creator.helpers.random_name import random_names
from creator.models import (Investigator, Occupation, Skills, Inventory, Item)


User = get_user_model()


def amount(points_available: int, limit: int):
    """Generate an adequate random value for the points assignment."""
    limit = min(points_available, 91-limit)
    val = randint(1, limit)
    return val


def get_occupation_skills(inv: Investigator):
    """Based on the investigators occupation determine the list of skills."""
    # Generate list of skills
    occupation_skills = []
    # obtain list of all basic skills
    all_skills = list(inv.skills.keys())
    # assign the mandatories
    occupation_skills.extend(inv.occupation.skills.get('basics'))
    # assign extra categories with their limits
    skill_types = [
        category.replace("limit_", "") for category
        in list(inv.occupation.skills.keys()) if 'limit' in category
    ]
    for stype in skill_types:
        limit_key = f'limit_{stype}'
        limit = inv.occupation.skills.get(limit_key)
        if stype == 'free':
            skills_by_category = all_skills
        else:
            skills_key = f'skill_{stype}'
            skills_by_category = []
            raw_skills = inv.occupation.skills.get(
                skills_key
            )
            for skill in raw_skills:
                # validate they are skills and not skill categories
                if skill in all_skills:
                    skills_by_category.append(skill)
                else:
                    skills = [
                        sk for sk in all_skills if skill in sk
                    ]
                    skills_by_category.extend(skills)
            
        for _ in range(limit):
            if skills_by_category is not None:
                skill = choice(skills_by_category) 
                occupation_skills.append(
                    skill
                )
            else:
                msg = "Occupation: {} has no skills at category {}".format(
                    inv.occupation.title,
                    stype
                )
                raise Exception(msg)
                
    return occupation_skills


def occ_point_assigner(max_points: int, inv: Investigator):
    """Assign points for the skills related to occupations."""
    # Assing profession points

    occupation_skills = get_occupation_skills(inv)
    val = (max_points // 2) // len(occupation_skills)
    for occ_skill in occupation_skills:
        inv.skills[occ_skill]['value'] += val
        max_points -= val

    shuffle(occupation_skills)
    while max_points:
        occ_skill = choice(occupation_skills)
        skill = inv.skills[occ_skill]
        base_value = skill.get('value')
        val = amount(max_points, base_value)
        if (base_value + val) < 90 and (max_points - val) >= 0:
            inv.skills[occ_skill]['value'] += val
            max_points -= val

    inv.skills['Credit Rating']['value'] = randint(
        inv.occupation.credit_rating_min,
        inv.occupation.credit_rating_max
    )
    inv.skills['Language(Own)']['value'] = inv.education
    inv.skills['Dodge']['value'] = inv.dexterity // 2
    inv.save()


def free_point_assigner(max_points: int, inv: Investigator):
    """Assign points to any skill."""
    skills = list(inv.skills.keys())
    while max_points:
        skill = choice(skills)
        if skill == "Credit Rating":
            continue
        base_value = inv.skills[skill]['value']
        val = amount(max_points, base_value)
        if (base_value + val) < 90 and (max_points - val) >= 0:
            inv.skills[skill]['value'] += val
            max_points -= val
    inv.save()


def base_skills_generator(skills: list, inv: Investigator):
    '''Generate a default skill dict for the investigator.'''
    for skill in skills:
        sub_skills = skill.sub_skills
        if sub_skills:
            #category skills
            for sub_skill in sub_skills:
                skill_name = f"{skill.title}({sub_skill})"
                sub_skill_val = skill.sub_skills[sub_skill].get('base_value')
                if sub_skill_val is None:
                    inv.skills[skill_name] = {
                        'value': skill.base_value
                    }
                else:
                    inv.skills[skill_name] = {
                        'value': sub_skill_val
                    }
                    
            pass
        else:
            inv.skills[skill.title] = {
                'value': skill.base_value
            }
    
    inv.save()


def random_inv():
    """Main wrapper."""
    # Pick a random occupation
    occupations = Occupation.objects.all()
    occupation = choice(occupations)
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
        "occupation": occupation,
        "ideologies": "Atheist",
        "luck": roller_stats(3),
        "skills": {}
    }
    inv = Investigator(**attrs)
    inv.save()
    # Produce attributes
    inv.strength = roller_stats(3)
    inv.dexterity = roller_stats(3)
    inv.constitution = roller_stats(3)
    inv.power = roller_stats(3)
    inv.size = roller_stats(2)
    inv.education = roller_stats(2)
    inv.intelligence = roller_stats(2)
    inv.appearance = roller_stats(3)
    # Load derivative statuses
    inv.health = inv.max_health
    inv.sanity = inv.power
    inv.save()
    # Gerenarte base skills
    skills = list(Skills.objects.filter(year="1920's"))
    base_skills_generator(skills, inv)
    # Assign points to occupation skills
    proff_points = inv.occupation_skill_points
    occ_point_assigner(proff_points, inv)
    # Assign free skill points
    free_point_assigner(inv.free_skill_points, inv)
    # Assign a weapon
    weapons = Item.objects.filter(
        category=3,
        properties__subcategory__in=[
            'Handguns',
            'Hand-to-Hand'
        ]
    )
    weapon = choice(weapons)
    inventory = Inventory(
        investigator=inv,
        item=weapon
    )
    inventory.save()
    # Create an inventory
    # assign random items (consumables or tools)
    items = Item.objects.filter(category__in=[2, 4])
    for _ in range(5):
        inventory = Inventory(
            investigator=inv,
            item=choice(items)
        )
        inventory.save()
    return inv.uuid
