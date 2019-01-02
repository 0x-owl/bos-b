from django.db.models import (BooleanField, CASCADE, CharField, ForeignKey,
                              IntegerField, Model, PositiveIntegerField)
from django.core.validators import MaxValueValidator

from creator.constants import GENDER


# Create your models here.
class Skills(Model):
    title = CharField(max_length=50)
    value = PositiveIntegerField(default=0)


#  class Occupation(Model):
    #  title = CharField(max_length=50)
    #  attributes = 


class InvestigatorSkills(Model):
    """Basic skills."""
    accounting = PositiveIntegerField(
            default=5, validators=[MaxValueValidator(99)])
    anthropology = PositiveIntegerField(
        default=1, validators=[MaxValueValidator(99)])
    appraise = PositiveIntegerField(
        default=5, validators=[MaxValueValidator(99)])
    archaelogy = PositiveIntegerField(
        default=1, validators=[MaxValueValidator(99)])
    art_craft = PositiveIntegerField(
        default=5, validators=[MaxValueValidator(99)])
    charm = PositiveIntegerField(
        default=15, validators=[MaxValueValidator(99)])
    climb = PositiveIntegerField(
        default=20, validators=[MaxValueValidator(99)])
    credit_rating = PositiveIntegerField(
        default=0, validators=[MaxValueValidator(99)])
    cthulhu_mythos = PositiveIntegerField(
        default=0, validators=[MaxValueValidator(99)])
    disguise = PositiveIntegerField(
        default=5, validators=[MaxValueValidator(99)])
    dodge = PositiveIntegerField(
        default=0, validators=[MaxValueValidator(99)])
    drive_auto = PositiveIntegerField(
        default=20, validators=[MaxValueValidator(99)])
    elec_repair = PositiveIntegerField(
        default=10, validators=[MaxValueValidator(99)])
    fast_talk = PositiveIntegerField(
        default=5, validators=[MaxValueValidator(99)])
    fighting_brawl = PositiveIntegerField(
        default=25, validators=[MaxValueValidator(99)])
    firearms_handgun = PositiveIntegerField(
        default=20, validators=[MaxValueValidator(99)])
    firearms_shotgun_rifle = PositiveIntegerField(
        default=25, validators=[MaxValueValidator(99)])
    first_aid = PositiveIntegerField(
        default=30, validators=[MaxValueValidator(99)])
    history = PositiveIntegerField(
        default=5, validators=[MaxValueValidator(99)])
    intimidate = PositiveIntegerField(
        default=15, validators=[MaxValueValidator(99)])
    jump = PositiveIntegerField(
        default=0, validators=[MaxValueValidator(99)])
    language_other = PositiveIntegerField(
        default=1, validators=[MaxValueValidator(99)])
    language_own = PositiveIntegerField(
        default=0, validators=[MaxValueValidator(99)])
    law = PositiveIntegerField(default=5, validators=[MaxValueValidator(99)])
    library_use = PositiveIntegerField(
        default=20, validators=[MaxValueValidator(99)])
    listen = PositiveIntegerField(
        default=20, validators=[MaxValueValidator(99)])
    locksmith = PositiveIntegerField(
        default=1, validators=[MaxValueValidator(99)])
    mech_repair = PositiveIntegerField(
        default=10, validators=[MaxValueValidator(99)])
    medicine = PositiveIntegerField(
        default=1, validators=[MaxValueValidator(99)])
    natural_world = PositiveIntegerField(
        default=10, validators=[MaxValueValidator(99)])
    navigate = PositiveIntegerField(
        default=10, validators=[MaxValueValidator(99)])
    occult = PositiveIntegerField(
        default=5, validators=[MaxValueValidator(99)])
    op_hv_machine = PositiveIntegerField(
        default=1, validators=[MaxValueValidator(99)])
    persuade = PositiveIntegerField(
        default=10, validators=[MaxValueValidator(99)])
    pilot = PositiveIntegerField(
        default=1, validators=[MaxValueValidator(99)])
    psychology = PositiveIntegerField(
        default=10, validators=[MaxValueValidator(99)])
    psychoanalysis = PositiveIntegerField(
        default=1, validators=[MaxValueValidator(99)])
    ride = PositiveIntegerField(
        default=5, validators=[MaxValueValidator(99)])
    science = PositiveIntegerField(
        default=1, validators=[MaxValueValidator(99)])
    sleight_of_hand = PositiveIntegerField(
        default=10, validators=[MaxValueValidator(99)])
    spot_hidden = PositiveIntegerField(
        default=25, validators=[MaxValueValidator(99)])
    stealth = PositiveIntegerField(
        default=20, validators=[MaxValueValidator(99)])
    survival = PositiveIntegerField(
        default=10, validators=[MaxValueValidator(99)])
    swim = PositiveIntegerField(default=20, validators=[MaxValueValidator(99)])
    throw = PositiveIntegerField(
        default=20, validators=[MaxValueValidator(99)])
    track = PositiveIntegerField(
        default=10, validators=[MaxValueValidator(99)])


class Investigator(Model):
    """Investigators class."""
    name = CharField(max_length=50)
    player = CharField(max_length=50)
    sex = CharField(max_length=1, choices=GENDER)
    residence = CharField(max_length=80)
    birthplace = CharField(max_length=80)
    age = PositiveIntegerField(default=18)
    strength = PositiveIntegerField()
    dexterity = PositiveIntegerField()
    power = PositiveIntegerField()
    constitution = PositiveIntegerField()
    appearence = IntegerField()
    education = IntegerField()
    size = IntegerField()
    luck = PositiveIntegerField()
    intelligence = IntegerField()
    occupation = ForeignKey('Occupation', on_delete=CASCADE)

    @property
    def health(self):
        """Health property."""
        health = (self.size + self.constitution) // 10
        return health

    @property
    def sanity(self):
        """Sanity property."""
        return self.power

    @property
    def magic_points(self):
        """Magic points property."""
        mp = self.power // 5
        return mp

    @property
    def move(self):
        """Move rate property."""
        dex = self.dexterity
        siz = self.size
        strg = self.strength
        if strg >= siz or dex >= siz:
            mov = 8
        elif strg > siz and dex > siz:
            mov = 9
        else:
            mov = 7

        if self.age // 10 >= 4:
            mov = mov - ((self.age // 10) - 3)

        return mov
