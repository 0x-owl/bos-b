from django.http import HttpResponse
from django.shortcuts import render, redirect

from random import choice
from json import dumps

from creator.random_inv import RandomInvestigator
from creator.constants import SILOUETTES as silouettes
from creator.helpers.views_helper import generate_basic_info_form

from creator.helpers.investigator import generate_full_half_fifth_values

from creator.models import (
    Investigator, Skills, Portrait, Inventory, PhobiaInvestigator,
    ManiaInvestigator, SpellInvestigator
)


# Create your views here.
def get_investigator_data(request, inv, **kwargs):
    '''Retrieve all information associated to an
    Investigator.'''
    investigator = Investigator.objects.get(
        uuid=inv
    )
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
    weapons = Inventory.objects.filter(
        investigator=investigator,
        item__category=3)
    for weapon in weapons:
        weapon.properties['skill_value'] = generate_full_half_fifth_values(
            investigator.skills[weapon.item.properties['skill']]['value']
        )
    res['weapons'] = weapons

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
    form = generate_basic_info_form(request, investigator)
    if request.method == 'POST':
        # This redirect forces a full update of the character sheet data and
        # pulling a get request instead of being a post and making easier the
        # reload 
        return redirect(get_investigator_data, inv=investigator.uuid)
    return render(
        request, 'character_sheet.html',
        {'res': res, 'form': kwargs.get('form', form)})


def generate_random_investigator(request):
    rand = RandomInvestigator()
    rand.build()
    return redirect(get_investigator_data, inv=rand.investigator.uuid)