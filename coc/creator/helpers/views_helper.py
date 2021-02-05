from creator.forms import InvestigatorBasicInfoForm
from creator.models import Investigator

# Update investigators basic info
def generate_basic_info_form(request, inv):
    '''Method generate or update the investigator basic information form.'''
    if request.method == "POST":
        form = InvestigatorBasicInfoForm(request.POST)
        if form.is_valid():
            inv = Investigator.objects.filter(
                uuid=inv.uuid
            )
            data = form.cleaned_data
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
                'age': inv.age
            })
    

    return form