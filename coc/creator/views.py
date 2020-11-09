from django.http import HttpResponse
from django.shortcuts import render

from creator.models import Investigator, Skills, InvestigatorSkills

from json import dumps
# Create your views here.

def get_investigator_data(request, inv):
    '''Retrieve all information associated to an
    Investigator.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    res = {
        'name': investigator.name,
        'sex': investigator.sex,
        'age': investigator.age,
        'birthplace': investigator.birthplace,
        'residence': investigator.residence,
        'size': investigator.size,
        'occupation': {
            'title': investigator.occupation.title,
            'credit_rating_min': investigator.occupation.credit_rating_min,
            'credit_rating_max': investigator.occupation.credit_rating_max,
            'contacts': investigator.occupation.suggested_contacts,
        },
        'attributes': {
            'dex': investigator.dexterity,
            'str': investigator.strength,
            'con': investigator.constitution,
            'app': investigator.appearance,
            'int': investigator.intelligence,
            'pow': investigator.power,
            'edu': investigator.education,
            'size': investigator.size,
            'sanity': investigator.sanity,
            'max_health': investigator.max_health,
            'health': investigator.health,
            'magic_points': investigator.magic_points,
            'move_rate': investigator.move,
            'build': investigator.build[1],
            'modifier': investigator.build[0]
        },
    }
    skills_dict = {}
    inv_skills = InvestigatorSkills.objects.filter(
        investigator=investigator
    )
    for skill in inv_skills:
        skills_dict[skill.skill.title] = {
            'value': skill.value,
            'category': skill.category
        }
    res['skills'] = skills_dict

    return HttpResponse(dumps(res))