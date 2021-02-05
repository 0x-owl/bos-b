from django.forms import Form, CharField, IntegerField, TextInput
from creator.constants import GENDER

class InvestigatorBasicInfoForm(Form):
    '''Basic information form for an Investigator.'''
    name = CharField(
        max_length=50,
        widget=TextInput(attrs={
            'class': 'form-control',
            'aria-describedby': "inv-name"})
    )
    player = CharField(
        max_length=50,
        widget=TextInput(attrs={
            'class': 'form-control',
            'aria-describedby': "inv-name"}))
    sex = CharField(
        max_length=1,
        widget=TextInput(attrs={
            'class': 'form-control',
            'aria-describedby': "inv-sex"})
    )
    residence = CharField(
        max_length=80,
        widget=TextInput(attrs={
            'class': 'form-control',
            'aria-describedby': 'inv-residence'})
    )
    birthplace = CharField(
        max_length=80,
        widget=TextInput(attrs={
            'class': 'form-control',
            'aria-describedby': 'inv-birthplace'})
    )
    age = IntegerField(
        max_value=90,
        widget=TextInput(attrs={
            'class': 'form-control',
            'aria-describedby': 'inv-age'})
    )