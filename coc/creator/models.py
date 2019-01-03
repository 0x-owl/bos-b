from django.db.models import (BooleanField, CASCADE, CharField, ForeignKey,
                              IntegerField, Model, PositiveIntegerField)
from django.core.validators import MaxValueValidator

from creator.constants import GENDER


# Create your models here.
class Occupation(Model):
    """Occupation class."""
    title = CharField(max_length=50)


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
    occupation = ForeignKey(Occupation, on_delete=CASCADE)


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
        """Move rate property, affected by certain conditions."""
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


    @property
    def build(self):
        """Build attribute property."""
        amount = self.strength + self.size
        res = ()
        if amount <= 64:
            res = ('-2', -2)
        elif amount <= 84:
            res = ('-1', -1)
        elif amount <= 124:
            res = ('0', 0)
        elif amount <= 164:
            res = ('+1D4', 1)
        elif amount <= 204:
            res = ('+1D6', 2)
        elif amount <= 284:
            res = ('+2D6', 3)
        else:
            mod = (amount - 205) // 80
            dices = '{}D6'.format(mod+2)
            build = 3 + mod
            res = (dices, build)

        return res



class Skills(Model):
    title = CharField(max_length=50)
    value = PositiveIntegerField(default=0)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
