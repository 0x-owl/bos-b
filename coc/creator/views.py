from json import dumps
from random import choice

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from creator.constants import SILOUETTES as silouettes
from creator.helpers.investigator import generate_full_half_fifth_values
from creator.helpers.views_helper import (generate_basic_info_form,
                                          generate_derivative_attributes_form)
from creator.models import (Inventory, Investigator, ManiaInvestigator,
                            Occupation, PhobiaInvestigator, Portrait, Skills,
                            SpellInvestigator)
from creator.random_inv import RandomInvestigator


# Create your views here.
def get_investigators_data(request, inv, **kwargs):
    '''Retrieve all information associated to an
    Investigator.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    res = {
        'investigator': investigator
    }
    # Retrieve manias and phobias
    manias = ManiaInvestigator.objects.filter(
        investigator=investigator
    )
    phobias = PhobiaInvestigator.objects.filter(
        investigator=investigator
    )
    res['manias'] = manias
    res['phobias'] = phobias
    # Retrieve arcane
    artifacts = Inventory.objects.filter(
        investigator=investigator,
        item__category=1

    )
    spells = SpellInvestigator.objects.filter(
        investigator=investigator
    )
    res['arcane'] = {
        'artifacts': artifacts,
        'spells': spells  
    }
    derivative_attrs_form = generate_derivative_attributes_form(
        request, investigator)
    if request.method == 'POST':
        # This redirect forces a full update of the character sheet data and
        # pulling a get request instead of being a post and making easier the
        # reload 
        return redirect(get_investigators_data, inv=investigator.uuid)
    return render(
        request, 'character_sheet.html',
        {
            'res': res,
            'derivative_attrs_form': derivative_attrs_form
        }
    )


def investigators_basic_info(request, inv):
    '''Generate investigator basic information form.'''
    investigator = generate_basic_info_form(
        request, inv)
    occupations = [
        [occ.uuid, occ.__str__()] for occ in 
        Occupation.objects.all()
    ]
    investigator = {
        'name': investigator.name,
        'uuid': investigator.uuid,
        'sex': investigator.sex,
        'occupation': investigator.occupation.uuid,
        'age': investigator.age,
        'player': investigator.player,
        'residence': investigator.residence,
        'birthplace': investigator.birthplace
    }
    return JsonResponse(
        {
            'investigator': investigator,
            'occupations': occupations
        },
        status=200
    )


def get_investigators_attributes(request, inv):
    '''Retrieve investigators attributes.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    attributes = investigator.attributes_detail
    attributes['MOV'] = [investigator.move]
    attributes["BUILD"] = list(investigator.build)
    return JsonResponse(
        {'attributes': attributes}, status=200)


def get_investigators_portrait(request, inv):
    '''Retrieve investigators portrait.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    portrait = Portrait.objects.filter(
        investigator=investigator
    ).first()
    default_portrait = silouettes[0] if investigator.sex == 'M' else silouettes[1]

    res = {'portrait': portrait.portrait.url if portrait is not None else default_portrait}
    return JsonResponse(res, status=200)


def get_investigators_deriv_attrs(request, inv):
    '''Generate investigator derivative attributes form.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    form = generate_derivative_attributes_form(
        request, investigator)
    return render(
        request, 'inv_basic_info.html',
        {'derivative_attrs_form': form}
    )


def get_investigators_skills(request, inv):
    investigator = Investigator.objects.get(
        uuid=inv
    )
    # Retrieve skills
    skills = sorted(investigator.skills)
    skills_sanitized = []
    for skill in skills:
        skills_sanitized.append(
            [
                skill,
                *generate_full_half_fifth_values(
                    investigator.skills[skill]['value']
                )
            ]
        )
    res = {'skills': skills_sanitized}
    return JsonResponse(res, status=200)


def get_investigators_weapons(request, inv):
    '''Retrieve investigators weapons.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    weapons = Inventory.objects.filter(
        investigator=investigator,
        item__category=3)
    weapons_results = []
    for weapon in weapons:
        w_dict = weapon.properties
        w_dict['skill_value'] = generate_full_half_fifth_values(
            investigator.skills[weapon.item.properties['skill']]['value']
        )
        weapons_results.append(w_dict)
    return JsonResponse({'weapons': weapons_results}, status=200)


def get_investigators_gear(request, inv):
    '''Retrieve investigators gear.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    items = Inventory.objects.filter(
        investigator=investigator,
        item__category__in=[2,4]
    )
    gear = [
        {
            'title': item.properties['title'],
            'stock': item.stock,
            'price': item.properties['price']
        } for item in items
    ]
    return JsonResponse({'gear': gear}, status=200)


def get_investigators_manias_and_phobias(request, inv):
    '''Retrieve investigators manias and phobias.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    manias = ManiaInvestigator.objects.filter(
        investigator=investigator
    )
    phobias = PhobiaInvestigator.objects.filter(
        investigator=investigator
    )
    res = {}
    res['manias'] = manias
    res['phobias'] = phobias
    return JsonResponse(res, status=200)


def get_investigators_arcane(request, inv):
    '''Retrieve arcane artifacts and spells from investigator.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    # Retrieve arcane
    artifacts = Inventory.objects.filter(
        investigator=investigator,
        item__category=1

    )
    spells = SpellInvestigator.objects.filter(
        investigator=investigator
    )
    res = {}
    res['arcane'] = {
        'artifacts': artifacts,
        'spells': spells  
    }
    return JsonResponse(res, status=200)


def generate_random_investigator(request):
    rand = RandomInvestigator()
    rand.build()
    return redirect(get_investigators_data, inv=rand.investigator.uuid)
