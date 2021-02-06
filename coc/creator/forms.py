from django.forms import Form, CharField, ChoiceField, IntegerField, TextInput, Select, NumberInput
from creator.models import Occupation
from creator.constants import GENDER

class InvestigatorBasicInfoForm(Form):
    '''Basic information form for an Investigator.'''
    name = CharField(
        max_length=50,
        widget=TextInput(attrs={
            'class': 'form-control',
            'aria-describedby': "inv-name"})
    )
    sex = ChoiceField(
        choices=[
            ('F', 'Female'),
            ('M', 'Male')
        ],
        widget=Select(
            attrs={
                'class': 'form-control',
                'aria-describedby': "inv-sex"})
    )
    player = CharField(
        max_length=50,
        widget=TextInput(attrs={
            'class': 'form-control',
            'aria-describedby': "inv-player"})
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
        widget=NumberInput(attrs={
            'class': 'form-control',
            'aria-describedby': 'inv-age',
            'min': 15,
            'max': 90
        })
    )
    occupation = ChoiceField(
        choices=[
            (occupation.uuid, occupation.title) for occupation
            in Occupation.objects.all()
        ],
        widget=Select(attrs={
            'class': 'form-control',
            'aria-desribedby': 'inv-occupation'
        })
    )