from django.http import HttpResponse
from django.shortcuts import render, redirect

from creator.helpers.random_investigator import random_inv
from creator.models import Investigator, Skills, Portrait, Inventory

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
        'portrait': portrait.portrait.url if portrait is not None else "",
        'attributes': investigator.attributes_detail,
        "inv": investigator
    }
    # Retrieve skills
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

    # Retrieve "inventory"
    weapons = Inventory.objects.filter(
        investigator=investigator, item__item_type = 3)

    items = Inventory.objects.filter(
        investigator=investigator,
        item__item_type__in=[1,2,4]
    )
    res['gear'] = items
    return render(request, 'character_sheet.html', {'res': res})


def generate_random_investigator(request):
    inv = random_inv()
    return redirect(get_investigator_data, inv=inv)