from uuid import uuid4

from django_enumfield.enum import EnumField

from django.db.models import (BooleanField, CASCADE, CharField, DateTimeField,
                              FloatField, ForeignKey, ImageField, Model,
                              OneToOneField, PROTECT, PositiveIntegerField,
                              SET_NULL, TextField, UUIDField)
from django.contrib.auth.models import User

from creator.enums import Attribute, ItemCategory, SpellCategory
from creator.constants import GAME_TYPE, GENDER
from creator.helpers.model_helpers import obtain_attribute_value, renamer


# Create your models here.
class Tag(Model):
    """Tag class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    title = CharField(max_length=50)
    user = ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        """String representation of the object."""
        return '#{}'.format(self.title)


class Spell(Model):
    """Spell class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=50)
    alternative_names = TextField(blank=True)
    description = TextField()
    deeper_magic = TextField(blank=True)
    notes = TextField(blank=True)
    # 15 POW, 2D6 Sanity, 14 Magic Points, 100 sacrifices.
    cost = CharField(max_length=80)
    casting_time = CharField(max_length=50)

    def __str__(self):
        return self.name


class SpellType(Model):
    """Association Spell with its category."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    spell = ForeignKey(Spell, on_delete=CASCADE)
    spell_type = EnumField(SpellCategory)

    def __str__(self):
        title = '{} - {}'.format(self.spell.name, self.spell_type)
        return title


class SpellTag(Model):
    """Tags assigned to the Spell."""
    tag = ForeignKey(Tag, on_delete=PROTECT)
    spell = ForeignKey(Spell, on_delete=CASCADE)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.tag.title, self.spell.name)
        return title


class Skills(Model):
    """Skills class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    title = CharField(max_length=50)
    description = TextField(blank=True)
    user = ForeignKey(User, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'skills'

    def __str__(self):
        """String representation of the object."""
        return self.title


class SkillTags(Model):
    """Tags assigned to skills."""
    tag = ForeignKey(Tag, on_delete=PROTECT)
    skills = ForeignKey(Skills, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'skill tags'

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.tag.title, self.skills.title)
        return title


class Occupation(Model):
    """Occupation class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    user = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=50)
    description = TextField(blank=True)
    suggested_contacts = TextField()
    credit_rating_min = PositiveIntegerField()
    credit_rating_max = PositiveIntegerField()

    def __str__(self):
        """String representation of the object."""
        return self.title


class OccupationAttribute(Model):
    """Relation between occupation and attribute."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    occupation = ForeignKey(Occupation, on_delete=CASCADE)
    attr = EnumField(Attribute)
    modifier = PositiveIntegerField()
    optional = BooleanField(default=False)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {} - {}'.format(
            self.occupation.title, self.attr, self.value)
        return title


class OccupationSkills(Model):
    """Skills relation with Occupation."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    occupation = ForeignKey(Occupation, on_delete=CASCADE)
    skill = ForeignKey(Skills, on_delete=PROTECT)

    class Meta:
        verbose_name_plural = 'occupation skills'

    def __str__(self):
        """String representation of the object."""
        title = '{} - {} - {}'.format(
            self.occupation.title, self.skill.title, self.value)
        return title


class OccupationTags(Model):
    """Tags assigned to occupations."""
    tag = ForeignKey(Tag, on_delete=PROTECT)
    occupation = ForeignKey(Occupation, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'occupation tags'

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.tag.title, self.occupation.title)
        return title


class Investigator(Model):
    """Investigators class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=50)
    player = CharField(max_length=50)
    sex = CharField(max_length=1, choices=GENDER)
    residence = CharField(max_length=80)
    birthplace = CharField(max_length=80)
    age = PositiveIntegerField(default=18)
    occupation = OneToOneField(
        Occupation, on_delete=SET_NULL, default=None, null=True)
    ideologies = TextField(blank=True)
    description = TextField(blank=True)
    traits = TextField(blank=True)
    injure_scars = TextField(blank=True)
    significant_people = TextField(blank=True)
    meaningful_locations = TextField(blank=True)
    treasured_possessions = TextField(blank=True)
    encounters_with_strange_entities = TextField(blank=True)

    @property
    def dexterity(self):
        """Dexterity attribute property that obtains the value for the
        investigator.
        """
        dex = obtain_attribute_value(
            self, InvestigatorAttribute, Attribute, 'DEX')
        return dex

    @property
    def strength(self):
        """Strength attribute property that obtains the value for the
        investigator.
        """
        str_ = obtain_attribute_value(
            self, InvestigatorAttribute, Attribute, 'STR')
        return str_

    @property
    def constitution(self):
        """Constitution attribute property that obtains the value for the
        investigator.
        """
        con = obtain_attribute_value(
            self, InvestigatorAttribute, Attribute, 'CON')
        return con

    @property
    def power(self):
        """Power attribute property that obtains the value for the
        investigator.
        """
        pow_ = obtain_attribute_value(
            self, InvestigatorAttribute, Attribute, 'PWR')
        return pow_

    @property
    def size(self):
        """Size attribute property that obtains the value for the
        investigator.
        """
        siz = obtain_attribute_value(
            self, InvestigatorAttribute, Attribute, 'SIZ')
        return siz

    @property
    def education(self):
        """Education attribute property that obtains the value for the
        investigator.
        """
        edu = obtain_attribute_value(
            self, InvestigatorAttribute, Attribute, 'EDU')
        return edu

    @property
    def intelligence(self):
        """Intelligence attribute property that obtains the value for the
        investigator.
        """
        int_ = obtain_attribute_value(
            self, InvestigatorAttribute, Attribute, 'INT')
        return int_

    @property
    def appearance(self):
        """Appearance attribute property that obtains the value for the
        investigator.
        """
        app = obtain_attribute_value(
            self, InvestigatorAttribute, Attribute, 'APP')
        return app

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
        mp = self.sanity // 5
        return mp

    @property
    def move(self):
        """Move rate property, affected by certain conditions."""
        if self.strength >= self.size or self.dexterity >= self.size:
            mov = 8
        elif self.strength > self.size and self.dexterity > self.size:
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
        """Obtain the amount of free skill points an investigator has."""
        return self.intelligence * 2

    @property
    def occupation_skill_points(self):
        """Based on the occupation obtain the amount of free skill points."""
        skill_points = 0
        # Obtain a list of the occupation attributes.
        occ_attr = [occ for occ in OccupationAttribute.objects.filter(
                       occupation__uuid=self.occupation.uuid)]
        # Generate a diccionary with the investigators attribute data.
        inv_attr = {reg.attr.name: reg.value for reg in
                    InvestigatorAttribute.objects.filter(
                        investigator_id=self.id)}
        optionals = [0]
        # Iterate through the occupation attributes and add the skill points if
        # they are compulsory, if not check the the bigger of the optionals and
        # add it to the accumulator.
        for attr in occ_attr:
            if not attr.optional:
                skill_points += inv_attr[attr.attr.name] * attr.modifier
            else:
                optionals.append(inv_attr[attr.attr.name] * attr.modifier)
        skill_points += max(optionals)

        return skill_points

    def __str__(self):
        """String representation of the object."""
        return '{} - {}'.format(self.player, self.name)


class Portrait(Model):
    """Investigators picture class."""
    investigator = OneToOneField(Investigator, on_delete=CASCADE)
    portrait = ImageField(upload_to=renamer)

    def __str__(self):
        """String representation of the object."""
        return self.investigator.name


class InvestigatorAttribute(Model):
    """Relation between investigator and its attributes."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    attr = EnumField(Attribute)
    value = PositiveIntegerField()

    @property
    def half_value(self):
        """Return half of attribute value."""
        return self.value // 2

    @property
    def fifth_value(self):
        """Return fifth of attribute value."""
        return self.value // 5

    def __str__(self):
        """String representation of the object."""
        title = '{} - {} - {}'.format(
            self.investigator.name, self.attr, self.value)
        return title


class InvestigatorSkills(Model):
    """Skills relation with investigator class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    skill = ForeignKey(Skills, on_delete=PROTECT)
    value = PositiveIntegerField(default=0)

    @property
    def half_value(self):
        """Return half of attribute value."""
        return self.value // 2

    @property
    def fifth_value(self):
        """Return fifth of attribute value."""
        return self.value // 5

    class Meta:
        verbose_name_plural = 'investigator skills'

    def __str__(self):
        """String representation of the object."""
        title = '{} - {} - {}'.format(
            self.investigator.name, self.skill.title, self.value)
        return title


class InvestigatorTags(Model):
    """Tags assigned to investigators."""
    tag = ForeignKey(Tag, on_delete=PROTECT)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'investigator tags'

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.tag.title, self.investigator.name)
        return title


class InvestigatorsDiary(Model):
    """Investigators diary"""
    title = CharField(max_length=30, blank=True, null=True)
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    notes = TextField(blank=True)
    timestamp = DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the object."""
        time = self.timestamp.strftime("%Y-%m-%d-%H:%M:%S")
        user = self.investigator.user.username
        title = '{} - {} - {}'.format(time, self.investigator.name, user)
        return title


class TagDiary(Model):
    """Tag assigned to the Diary"""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    diary = ForeignKey(InvestigatorsDiary, on_delete=CASCADE)
    tag = ForeignKey(Tag, on_delete=PROTECT)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.tag.title, self.diary.title)
        return title


class Item(Model):
    """Item class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    title = CharField(max_length=50)
    item_type = EnumField(ItemCategory)
    description = TextField(blank=True)
    price = FloatField(default=0)

    def __str__(self):
        """String representation of the object."""
        return self.title


class ItemTag(Model):
    """Tags assigned to the Item."""
    tag = ForeignKey(Tag, on_delete=PROTECT)
    item = ForeignKey(Item, on_delete=CASCADE)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.tag.title, self.item.title)
        return title


class ItemImage(Model):
    """Items image."""
    item = OneToOneField(Item, on_delete=CASCADE)
    image = ImageField(upload_to=renamer)

    def __str__(self):
        """String representation of the object."""
        return self.item.title


class Weapon(Item):
    """Weapon model."""
    damage = CharField(max_length=50)
    base_range = CharField(max_length=30, default="Touch")
    uses_per_round = CharField(max_length=10, default="1")
    # 999 stands for no malfunction.
    mal_function = PositiveIntegerField(default=999)

    def __str__(self):
        return self.title


class WeaponSkill(Model):
    """Weapons require a skill to be used."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    weapon = ForeignKey(Weapon, on_delete=CASCADE)
    skill = ForeignKey(Skills, on_delete=CASCADE)

    def __str__(self):
        """String representation of object."""
        title = '{} {}'.format(self.weapon.title, self.skill.title)
        return title


class WeaponTag(Model):
    """Weapons can have tags related to the era they are used."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    weapon = ForeignKey(Weapon, on_delete=CASCADE)
    tag = ForeignKey(Tag, on_delete=PROTECT)

    def __str__(self):
        """String representation of object."""
        title = '#{} {}'.format(self.tag.title, self.weapon.title)
        return title


class WeaponImage(Model):
    """Weapons image."""
    weapon = OneToOneField(Weapon, on_delete=CASCADE)
    image = ImageField(upload_to=renamer)

    def __str__(self):
        """String representation of the object."""
        return self.weapon.title


class Inventory(Model):
    """Inventory class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    item = ForeignKey(Item, on_delete=CASCADE, null=True, blank=True)
    stock = PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Inventories'

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.item.title, self.investigator.name)
        return title


class Game(Model):
    """Game class."""
    title = CharField(max_length=80)
    description = TextField()
    user = ForeignKey(User, on_delete=CASCADE)
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    timestamp = DateTimeField(auto_now_add=True)
    game_type = CharField(max_length=1, choices=GAME_TYPE)

    def __str__(self):
        """String representation of the object."""
        return self.title


class CampaignInvestigator(Model):
    """Campaign Investigator Relationship"""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    campaign = ForeignKey(Game, on_delete=CASCADE)
    timestamp = DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.campaign.title, self.investigator.name)
        return title

class Mania(Model):
    """Manias class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    title = CharField(max_length=50)
    description = TextField()

    def __str__(self):
        """String representation of the object."""
        return self.title

class ManiaInvestigator(Model):
    """Manias  Investigator Relationship"""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    mania = ForeignKey(Mania, on_delete=CASCADE)
    #Undefined limit 999999
    duration = PositiveIntegerField(default=1)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {} - {}'.format(self.mania.title, self.investigator.name, self.duration)
        return title

class Phobia(Model):
    """Phobias class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    title = CharField(max_length=50)
    description = TextField()

    def __str__(self):
        """String representation of the object."""
        return self.title

class PhobiaInvestigator(Model):
    """Phobias  Investigator Relationship"""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    phobia = ForeignKey(Phobia, on_delete=CASCADE)
    #Undefined limit 999999
    duration = PositiveIntegerField(default=1)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {} - {}'.format(self.phobias.title, self.investigator.name, self.duration)
        return title
