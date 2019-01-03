from uuid import uuid4

from creator.constants import GENDER

from django.db.models import (BooleanField, CASCADE, CharField, ForeignKey,
                              Model, OneToOneField, PositiveIntegerField,
                              UUIDField)
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Occupation(Model):
    """Occupation class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    title = CharField(max_length=50)
    credit_rating_min = PositiveIntegerField()
    credit_rating_max = PositiveIntegerField(
        validators=[MinValueValidator(self.credit_rating_min + 1)]
    )

class Attributes(Model):
    """Attribute class model."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    name = CharField(max_length=20)


class OccupationAttribute(Model):
    """Relation between occupation and attribute."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    occupation = ForeignKey(Occupation, on_delete=CASCADE)
    attribute = ForeignKey(Attribute, on_delete=CASCADE)
    modifier = PositiveIntegerField()


class Investigator(Model):
    """Investigators class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    name = CharField(max_length=50)
    player = CharField(max_length=50)
    sex = CharField(max_length=1, choices=GENDER)
    residence = CharField(max_length=80)
    birthplace = CharField(max_length=80)
    age = PositiveIntegerField(default=18)
    # TODO: move this attributes to their own table
    # TODO: update the methods that use them
    strength = PositiveIntegerField()
    dexterity = PositiveIntegerField()
    power = PositiveIntegerField()
    constitution = PositiveIntegerField()
    appearence = PositiveIntegerField()
    education = PositiveIntegerField()
    size = PositiveIntegerField()
    luck = PositiveIntegerField()
    intelligence = PositiveIntegerField()
    occupation = OneToOneField(Occupation)

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

    @property
    def free_skill_points(self):
        return self.intelligence.value * 2

    @property
    def occupation_skill_points(self):
        # TODO: obtain the skills of the occupation and calculate the points
        # available
        pass


class InvestigatorAttribute(Model):
    """Relation between investigator and attribute."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    attribute = ForeignKey(Attribute, on_delete=CASCADE)
    value = PositiveIntegerField()

    @property
    def half_value(self):
        """Return half of attribute value."""
        return self.value // 2

    @property
    def fifth_value(self):
        """Return fifth of attribute value."""
        return self.value // 5


class Skills(Model):
    """Skills class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    title = CharField(max_length=50)
    value = PositiveIntegerField(default=0)

class InvestigatorSkills(Model):
    """Skills relation with investigator class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    skill = ForeignKey(Skills, on_delete=CASCADE)

class OccupationSkills(Model):
    """Skills relation with Occupation."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    occupation = ForeignKey(Occupation, on_delete=CASCADE)
    skill = ForeignKey(Skills, on_delete=CASCADE)
