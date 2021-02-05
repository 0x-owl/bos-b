from django.forms import Form, CharField, IntegerField
from creator.constants import GENDER

class InvestigatorBasicInfoForm(Form):
    '''Basic information form for an Investigator.'''
    name = CharField(max_length=50)
    player = CharField(max_length=50)
    sex = CharField(max_length=1)
    residence = CharField(max_length=80)
    birthplace = CharField(max_length=80)
    age = IntegerField(max_value=90)  