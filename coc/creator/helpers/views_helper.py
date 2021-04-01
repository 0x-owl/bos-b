from creator.forms import (AttributesForm, DerivativeAttributesForm,
                           InvestigatorBasicInfoForm)
from creator.helpers.investigator import generate_full_half_fifth_values
from creator.models import (Inventory, Investigator, Item, Mania, Occupation,
                            Phobia, Skills, Spell)
from creator.random_inv import (base_skills_generator, free_point_assigner,
                                occ_point_assigner)

ALL_MODELS = {
    'occupations': Occupation,
    'spells': Spell,
    'items': Item,
    'skills': Skills,
    'manias': Mania,
    'phobias': Phobia
    }

def generate_basic_info_form(request, inv):
    '''Generate or update the investigator using the basic information form.'''
    inv = Investigator.objects.get(
        uuid=inv
    )
    if request.method == "POST":
        form = InvestigatorBasicInfoForm(request.POST)
        if form.is_valid():
            inv = Investigator.objects.get(
                uuid=inv.uuid
            )
            data = form.cleaned_data
            # This means the occupation has been requested for an update
            if data['occupation'] != inv.occupation:
                # save the new occupation
                inv.occupation = data['occupation']
                inv.save()
                # reset skill dict
                skills=Skills.objects.all()
                base_skills_generator(skills, inv)
                # assign points to the skills
                occ_point_assigner(inv.occupation_skill_points, inv)
                # assign the free skill points
                free_point_assigner(inv.free_skill_points, inv)
                del data['occupation']

            # update the rest of the attributes
            inv = Investigator.objects.filter(
                uuid=inv.uuid
            )
            inv.update(**data)
            inv = inv.first()
            inv.save()

    return inv

def generate_derivative_attributes_form(request, inv):
    '''Generate or update the investigators derivative attributes.'''
    inv = Investigator.objects.get(
        uuid=inv
    )
    if request.method == 'POST':
        form = DerivativeAttributesForm(request.POST)
        if form.is_valid():
            inv = Investigator.objects.filter(
                uuid=inv.uuid
            )
            data = form.cleaned_data
            inv.update(**data)
            inv = inv.first()
            inv.save()
    return inv

def generate_attributes_form(request, inv):
    '''Generate or update the investigators attributes.'''
    inv = Investigator.objects.get(
        uuid=inv
    )
    if request.method == 'POST':
        form = AttributesForm(request.POST)
        if form.is_valid():
            inv = Investigator.objects.filter(
                uuid=inv.uuid
            )
            data = form.cleaned_data
            inv.update(**data)
            inv = inv.first()
            inv.save()
    return inv

def skills_sanitizer(investigator):
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
    return skills_sanitized

def gear_sanitizer(investigator):
    items = Inventory.objects.filter(
        investigator=investigator,
        item__category__in=[2,4]
    )
    gear = [
        {
            'uuid': item.uuid,
            'title': item.properties['title'],
            'stock': item.stock,
            'price': item.properties['price']
        } for item in items
    ]
    return gear
