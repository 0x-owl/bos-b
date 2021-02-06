from creator.forms import DerivativeAttributesForm, InvestigatorBasicInfoForm
from creator.models import Investigator, Occupation, Skills
from creator.random_inv import (base_skills_generator, free_point_assigner,
                                occ_point_assigner)


def generate_basic_info_form(request, inv):
    '''Generate or update the investigator using the basic information form.'''
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
    else:
        form = InvestigatorBasicInfoForm(initial={
                'name': inv.name,
                'player': inv.player,
                'sex': inv.sex,
                'residence': inv.residence,
                'birthplace': inv.birthplace,
                'age': inv.age,
                'occupation': inv.occupation.uuid
            })
    
    return form

def generate_derivative_attributes_form(request, inv):
    '''Generate or update the investigators derivative attributes.'''
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
    else:
        form = DerivativeAttributesForm(
            initial={
                'health': inv.health,
                'sanity': inv.sanity,
                'magic_points': inv.magic_points,
                'luck': inv.luck
            }
        )
    return form
