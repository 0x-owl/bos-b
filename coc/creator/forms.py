from django.forms import (CharField, ChoiceField, Form, IntegerField,
                          ModelChoiceField, NumberInput, Select, TextInput)

from creator.constants import GENDER
from creator.models import Occupation


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
    occupation = ModelChoiceField(
        queryset=Occupation.objects.all(),
        widget=Select(attrs={
            'class': 'form-control',
            'aria-desribedby': 'inv-occupation'
        })
    )


class AttributesForm(Form):
    '''Form for the main attributes associated to an investigator.'''
    strength = IntegerField()
    dexterity = IntegerField()
    constitution = IntegerField()
    power = IntegerField()
    size = IntegerField()
    education = IntegerField()
    intelligence = IntegerField()
    appearance = IntegerField()


class DerivativeAttributesForm(Form):
    '''Form for the attributes that are initialized based on
    the investigators attributes.'''
    health = IntegerField()
    sanity = IntegerField()
    magic_points = IntegerField()
    luck = IntegerField()
