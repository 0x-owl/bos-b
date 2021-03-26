from json import dumps
from random import choice

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from creator.constants import SILOUETTES as silouettes
from creator.helpers.investigator import generate_full_half_fifth_values
from creator.helpers.views_helper import (gear_sanitizer,
                                          generate_attributes_form,
                                          generate_basic_info_form,
                                          generate_derivative_attributes_form,
                                          skills_sanitizer, ALL_MODELS as all_models)
from creator.models import (Inventory, Investigator, Item, ManiaInvestigator,
                            Occupation, PhobiaInvestigator, Portrait, Skills,
                            SpellInvestigator)
from creator.random_inv import (RandomInvestigator, base_skills_generator,
                                free_point_assigner, occ_point_assigner)


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

    return render(
        request, 'character_sheet.html',
        {'res': res}
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


def investigators_attributes(request, inv):
    '''Retrieve investigators attributes.'''
    inv = generate_attributes_form(
        request, inv
    )
    attributes = inv.attributes_detail
    attributes['MOV'] = [inv.move]
    attributes["BUILD"] = list(inv.build)
    return JsonResponse(
        {'attributes': attributes}, status=200)


def investigators_attribute_update(request, inv):
    '''Retrieve investigators attributes.'''
    inv = Investigator.objects.filter(uuid=inv)

    if request.POST:
        data_unclean = dict(request.POST)
        attr = list(data_unclean.keys())[0]
        attr_value = int(data_unclean[attr][0])
        inv.update(**{attr: attr_value})
        attributes = {attr: generate_full_half_fifth_values(attr_value)}
        inv = inv.first()
        attributes['MOV'] = [inv.move]
        attributes["BUILD"] = list(inv.build)
        return JsonResponse(attributes, status=200)
    return JsonResponse({'response': 'Unauthorized'}, status=401)


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


def investigators_deriv_attrs(request, inv):
    '''Generate investigator derivative attributes form.'''
    inv = generate_derivative_attributes_form(
        request, inv)
    investigator_relevant_data = {
        "health": inv.health,
        "magic_points": inv.magic_points,
        "luck": inv.luck,
        "sanity": inv.sanity
    }
    return JsonResponse(
        {'investigator': investigator_relevant_data},
        status=200
    )


def get_investigators_skills(request, inv):
    investigator = Investigator.objects.get(
        uuid=inv
    )
    # Retrieve skills
    skills_sanitized = skills_sanitizer(investigator)
    res = {'skills': skills_sanitized}
    return JsonResponse(res, status=200)


def update_investigators_skills(request, inv):
    investigator = Investigator.objects.get(
        uuid=inv
    )
    skills = request.POST.keys()
    for skill in skills:
        inv_sk = investigator.skills.get(skill)
        if inv_sk is not None:
            investigator.skills[skill]['value'] = int(request.POST[skill])
    investigator.save()
    skills_sanitized = skills_sanitizer(investigator)
    res = {'skills': skills_sanitized}
    return JsonResponse(res, status=200)


def update_investigators_skill(request, inv):
    '''Update a single skill for an investigator.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    data_unclean = dict(request.POST)
    skill = list(data_unclean.keys())[0]
    skill_value = data_unclean[skill][0]
    inv_sk = investigator.skills.get(skill)
    if inv_sk is not None:
        investigator.skills[skill]['value'] = int(skill_value)
    investigator.save()
    res = {skill: list(generate_full_half_fifth_values(int(skill_value)))}
    return JsonResponse(res, status=200)


def investigators_skills_reset(request, inv):
    investigator = Investigator.objects.get(
        uuid=inv
    )
    skills = list(Skills.objects.all())
    base_skills_generator(skills, investigator)
    skills_sanitized = skills_sanitizer(investigator)
    res = {'skills': skills_sanitized}
    return JsonResponse(res, status=200)


def investigators_skills_shuffle(request, inv):
    investigator = Investigator.objects.get(
        uuid=inv
    )
    skills = list(Skills.objects.all())
    base_skills_generator(skills, investigator)
    proff_points = investigator.occupation_skill_points
    occ_point_assigner(proff_points, investigator)
    # Assign free skill points
    free_point_assigner(investigator.free_skill_points, investigator)
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
        w_dict['uuid'] = weapon.uuid
        weapons_results.append(w_dict)
    return JsonResponse({'weapons': weapons_results}, status=200)


def get_investigators_gear(request, inv):
    '''Retrieve investigators gear.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    gear = gear_sanitizer(investigator)
    return JsonResponse({'gear': gear}, status=200)


def remove_investigators_gear(request, inventory):
    '''Remove inventory from investigator.'''
    inventory = Inventory.objects.get(uuid=inventory)
    inventory.delete()
    return JsonResponse({'response': 'Ok'}, status=200)


def edit_investigators_gear(request, inventory):
    '''Remove inventory from investigator.'''
    inventory = Inventory.objects.get(uuid=inventory)
    if request.POST:
        data = dict(request.POST)
        sanitize_data = {
            k: data[k][0] for k in data.keys()
            if k != 'stock'
        }
        inventory.stock = int(data.get('stock', [1])[0])
        inventory.properties.update(**sanitize_data)
        inventory.save()
        inventory.properties['stock'] = inventory.stock
        return JsonResponse(inventory.properties, status=200)
    return JsonResponse({'response': 'Unauthorized'}, status=401)


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
    phobias = [[phobia.uuid, phobia.title] for phobia in phobias]
    manias = [[mania.uuid, mania.title] for mania in manias]
    res = {
        'manias': manias,
        'phobias': phobias
    }
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
    spells = [
        {
            'name': spell.spell.name,
            'cost': spell.spell.cost,
            'casting_time': spell.spell.casting_time,
            'description': spell.spell.description,
            'deeper_magic': spell.spell.deeper_magic,
            'alternative_names': spell.spell.alternative_names
        }
        for spell in spells
    ]
    artifacts = [
        artifact.properties.title
        for artifact in artifacts
    ]
    res = {
        'artifacts': artifacts,
        'spells': spells,
        'encounters': investigator.encounters_with_strange_entities
    }
    return JsonResponse(res, status=200)


def get_investigators_backstory(request, inv):
    '''Retrieve arcane artifacts and spells from investigator.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
    res = {
        'description': investigator.description,
        'ideologies': investigator.ideologies,
        'significant_people': investigator.significant_people,
        'meaningful_locations': investigator.meaningful_locations,
        'treasured_possessions': investigator.treasured_possessions,
        'traits': investigator.traits,
        'injuries_scars': investigator.injure_scars,
        'encounters_with_strange_entities': investigator.encounters_with_strange_entities
    }
    return JsonResponse(res, status=200)


def update_investigators_backstory(request, inv):
    '''Update investigators backstory information.'''
    investigator = Investigator.objects.filter(
        uuid=inv
    )
    if request.POST:
        data = dict(request.POST)
        sanitize_data = {
            k: data[k][0] for k in data.keys()
        }
        investigator.update(**sanitize_data)
        investigator = investigator.first().__dict__
        res = {
            k: investigator[k] for k in sanitize_data
        }
        return JsonResponse(res, status=200)
    return JsonResponse({'response': 'Unauthorized'}, status=401)


def generate_random_investigator(request):
    rand = RandomInvestigator()
    rand.build()
    return redirect(get_investigators_data, inv=rand.investigator.uuid)


def generic_model_list(request, model_type):

    model = {
        'model_name': model_type,
        'records': all_models[model_type].objects.all()
    }

    return render(request, 'generic_detail.html', model)

def record_detail(request, id, model_name):

    rec = {
        'record': all_models[model_name].objects.get(uuid=id)
    }

    return render(request, 'record_detail.html', rec)
