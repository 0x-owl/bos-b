from creator.forms import InvestigatorBasicInfoForm
from creator.models import Investigator, Skills, Occupation
from creator.random_inv import base_skills_generator, occ_point_assigner, free_point_assigner

# Update investigators basic info
def generate_basic_info_form(request, inv):
    '''Method generate or update the investigator basic information form.'''
    if request.method == "POST":
        form = InvestigatorBasicInfoForm(request.POST)
        if form.is_valid():
            inv = Investigator.objects.get(
                uuid=inv.uuid
            )
            data = form.cleaned_data
            # This means the occupation has been requested for an update
            if data['occupation'] != inv.occupation.uuid:
                # save the new occupation
                inv.occupation = Occupation.objects.get(
                    uuid=data['occupation']
                )
                inv.save()
                # reset skill dict
                skills=Skills.objects.all()
                base_skills_generator(skills, inv)
                # assign points to the skills
                occ_point_assigner(inv.occupation_skill_points, inv)
                # assign the free skill points
                free_point_assigner(inv.free_skill_points, inv)
                del data['occupation']

            # if occupation changed reset occupation points and 
            # re assign skills
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