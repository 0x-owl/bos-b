from json import dumps
from random import choice

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from creator.constants import SILOUETTES as silouettes
from creator.helpers.investigator import generate_full_half_fifth_values
from creator.helpers.views_helper import (generate_basic_info_form,
                                          generate_derivative_attributes_form)
from creator.models import (Inventory, Investigator, ManiaInvestigator,
                            PhobiaInvestigator, Portrait, Skills,
                            SpellInvestigator)
from creator.random_inv import RandomInvestigator


# Create your views here.
def get_investigators_data(request, inv, **kwargs):
    '''Retrieve all information associated to an
    Investigator.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    # covered
    portrait = Portrait.objects.filter(
        investigator=investigator
    ).first()
    default_portrait = silouettes[0] if investigator.sex == 'M' else silouettes[1]

    res = {
        'portrait': portrait.portrait.url if portrait is not None else default_portrait,
        'attributes': investigator.attributes_detail,
        'investigator': investigator
    }
    # Retrieve skills
    skills = sorted(investigator.skills)
    skills_sanitized = []
    for skill in skills:
        skills_sanitized.append(
            (
                skill,
                *generate_full_half_fifth_values(
                    investigator.skills[skill]['value']
                )
            )
        )

    res['skills'] = skills_sanitized

    # Retrieve "inventory"
    # weapons = Inventory.objects.filter(
    #     investigator=investigator,
    #     item__category=3)
    # for weapon in weapons:
    #     weapon.properties['skill_value'] = generate_full_half_fifth_values(
    #         investigator.skills[weapon.item.properties['skill']]['value']
    #     )
    # res['weapons'] = weapons

    items = Inventory.objects.filter(
        investigator=investigator,
        item__category__in=[2,4]
    )
    res['gear'] = items
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
    basic_info_form = generate_basic_info_form(
        request, investigator)
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
            'basic_info_form': basic_info_form,
            'derivative_attrs_form': derivative_attrs_form
        }
    )


def get_investigators_basic_info(request, inv):
    '''Generate investigator basic information form.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    form = generate_basic_info_form(
        request, investigator)
    return render(
        request, 'inv_basic_info.html',
        {'basic_info_form': form}
    )


def get_investigators_attributes(request, inv):
    '''Retrieve investigators attributes.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    return JsonResponse({'attributes': investigator.attributes_detail})


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
    return JsonResponse(res)


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
            (
                skill,
                *generate_full_half_fifth_values(
                    investigator.skills[skill]['value']
                )
            )
        )

    res = {'skills': skills_sanitized}
    return JsonResponse(res)


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
    return JsonResponse({'gear': items})


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
    return JsonResponse(res)


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
    return JsonResponse(res)


def generate_random_investigator(request):
    rand = RandomInvestigator()
    rand.build()
    return redirect(get_investigator_data, inv=rand.investigator.uuid)
