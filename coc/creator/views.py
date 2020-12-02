from django.http import HttpResponse
from django.shortcuts import render, redirect

from creator.helpers.random_investigator import random_inv
from creator.models import Investigator, Skills, Portrait

from json import dumps
# Create your views here.

def get_investigator_data(request, inv):
    '''Retrieve all information associated to an
    Investigator.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    portrait = Portrait.objects.filter(
        investigator=investigator
    ).first()
    
    res = {
        'name': investigator.name,
        'sex': investigator.sex,
        'age': investigator.age,
        'birthplace': investigator.birthplace,
        'residence': investigator.residence,
        'size': investigator.size,
        'portrait': portrait.portrait.url if portrait is not None else "",
        'occupation': {
            'title': investigator.occupation.title,
            'credit_rating_min': investigator.occupation.credit_rating_min,
            'credit_rating_max': investigator.occupation.credit_rating_max,
            'contacts': investigator.occupation.suggested_contacts,
        },
        'attributes': {
            'attrs': investigator.attributes_detail,
            'size': investigator.size,
            'sanity': investigator.sanity,
            'max_health': investigator.max_health,
            'health': investigator.health,
            'magic_points': investigator.magic_points,
            'move_rate': investigator.move,
            'build': investigator.build[1],
            'modifier': investigator.build[0],
            'luck': investigator.luck
        }
    }
    skills = sorted(investigator.skills)
    skills_sanitized = []
    for skill in skills:
        skills_sanitized.append((
            skill,
            investigator.skills[skill]['value'],
            investigator.skills[skill]['value'] // 2,
            investigator.skills[skill]['value'] // 5
        ))
    res['skills'] = skills_sanitized
    

    return render(request, 'character_sheet.html', {'investigator': res})


def generate_random_investigator(request):
    inv = random_inv()
    return redirect(get_investigator_data, inv=inv)