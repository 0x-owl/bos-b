import django

from uuid import uuid4

from django.db.models import (BooleanField, CASCADE, CharField, DateTimeField,
                              FloatField, ForeignKey, ImageField, IntegerField,
                              Model, OneToOneField, PROTECT,
                              PositiveIntegerField, SET_NULL, TextField,
                              UUIDField, JSONField)
from django.contrib.auth import get_user_model

from creator.constants import GAME_TYPE, GENDER, ITEM_CATEGORIES, SPELL_CATEGORIES
from creator.helpers.model_helpers import renamer, roller_stats

User = get_user_model()

# Create your models here.
class BaseModel(Model):
    uuid = UUIDField(unique=True, default=uuid4, editable=False, primary_key=True)
    created = DateTimeField(default=django.utils.timezone.now, editable=False)
    modified = DateTimeField(auto_now=True, null=True)
    deleted = DateTimeField(default=None, null=True)

    class Meta:
        abstract=True


class Tag(BaseModel):
    """Tag class."""
    title = CharField(max_length=50)
    user = ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        """String representation of the object."""
        return '#{}'.format(self.title)


class Spell(BaseModel):
    """Spell class."""
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


class SpellType(BaseModel):
    """Association Spell with its category."""
    spell = ForeignKey(Spell, on_delete=CASCADE)
    spell_type = PositiveIntegerField(
            choices=SPELL_CATEGORIES
        )

    def __str__(self):
        title = '{} - {}'.format(self.spell.name, self.spell_type)
        return title


class SpellTag(BaseModel):
    """Tags assigned to the Spell."""
    tag = ForeignKey(Tag, on_delete=PROTECT)
    spell = ForeignKey(Spell, on_delete=CASCADE)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.tag.title, self.spell.name)
        return title


class Skills(BaseModel):
    """Skills class."""
    skills = JSONField()
    year = CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'skills'

    def __str__(self):
        """String representation of the object."""
        return self.year


class Occupation(BaseModel):
    """Occupation class."""
    title = CharField(max_length=50)
    description = TextField(blank=True)
    suggested_contacts = TextField()
    credit_rating_min = PositiveIntegerField()
    credit_rating_max = PositiveIntegerField()
    skills = JSONField()
    points = JSONField()
    
    def __str__(self):
        """String representation of the object."""
        return self.title


class OccupationTags(BaseModel):
    """Tags assigned to occupations."""
    tag = ForeignKey(Tag, on_delete=PROTECT)
    occupation = ForeignKey(Occupation, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'occupation tags'

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.tag.title, self.occupation.title)
        return title


class Investigator(BaseModel):
    """Investigators class."""
    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=50)
    player = CharField(max_length=50)
    sex = CharField(max_length=1, choices=GENDER)
    residence = CharField(max_length=80)
    birthplace = CharField(max_length=80)
    age = PositiveIntegerField(default=18)
    # Attributes
    strength = PositiveIntegerField(default=roller_stats(3))
    dexterity = PositiveIntegerField(default=roller_stats(3))
    constitution = PositiveIntegerField(default=roller_stats(3))
    power = PositiveIntegerField(default=roller_stats(3))
    size = PositiveIntegerField(default=roller_stats(2))
    education = PositiveIntegerField(default=roller_stats(2))
    intelligence = PositiveIntegerField(default=roller_stats(2))
    appearance = PositiveIntegerField(default=roller_stats(3))
    # Composition
    occupation = ForeignKey(
        Occupation, on_delete=SET_NULL, default=None, null=True)
    skills = JSONField()
    ideologies = TextField(blank=True)
    description = TextField(blank=True)
    traits = TextField(blank=True)
    injure_scars = TextField(blank=True)
    significant_people = TextField(blank=True)
    meaningful_locations = TextField(blank=True)
    treasured_possessions = TextField(blank=True)
    encounters_with_strange_entities = TextField(blank=True)
    sanity = PositiveIntegerField(default=0)
    luck = PositiveIntegerField(default=roller_stats(3))
    health = IntegerField(default=0)

    @property
    def max_health(self):
        """Health property."""
        health = (self.size + self.constitution) // 10
        return health

    @property
    def magic_points(self):
        """Magic points property."""
        mp = self.sanity // 5
        return mp

    @property
    def attributes_detail(self):
        """Return attributes with their, full, half, fifth values."""
        attributes = {
            'STR': (self.strength, self.strength // 2, self.strength // 5),
            'DEX': (self.dexterity, self.dexterity // 2, self.dexterity // 5),
            'CON': (self.constitution, self.constitution // 2, self.constitution // 5),
            'POW': (self.power, self.power // 2, self.power // 5),
            'SIZ': (self.size, self.size // 2, self.size // 5),
            'EDU': (self.education, self.education // 2, self.education // 5),
            'INT': (self.intelligence, self.intelligence // 2, self.intelligence // 5),
            'APP': (self.appearance, self.appearance // 2, self.appearance // 5)
        }
        return attributes

    @property
    def move(self):
        """Move rate property, affected by certain conditions."""
        if self.strength > self.size and self.dexterity > self.size:
            mov = 9
        elif self.strength >= self.size or self.dexterity >= self.size:
            mov = 8
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
            dices = '{}D6'.format(mod + 2)
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
        occupation_points_formula = self.occupation.points
        inv_attrs = self.attributes_detail
        mandatories = occupation_points_formula['mandatory_attributes']
        optionals = occupation_points_formula['optional_attributes']
        for mandatory in mandatories:
            skill_points += inv_attrs[mandatory][0] * mandatories[mandatory]
        
        max_optional = 0
        for optional in optionals:
            value = inv_attrs[optional][0] * optionals[optional]
            max_optional = value if value > max_optional else max_optional
        
        skill_points += max_optional

        return skill_points


    def init_sanity(self):
        """Sanity property, start."""
        self.sanity = self.power
        self.save()
        ret = 'Sanity was initialized'
        return ret

    def __str__(self):
        """String representation of the object."""
        return '{} - {}'.format(self.player, self.name)


class Portrait(BaseModel):
    """Investigators picture class."""
    investigator = OneToOneField(Investigator, on_delete=CASCADE)
    portrait = ImageField(upload_to=renamer)

    def __str__(self):
        """String representation of the object."""
        return self.investigator.name


class InvestigatorTags(BaseModel):
    """Tags assigned to investigators."""
    tag = ForeignKey(Tag, on_delete=PROTECT)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'investigator tags'

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.tag.title, self.investigator.name)
        return title


class InvestigatorsDiary(BaseModel):
    """Investigators diary"""
    title = CharField(max_length=30, blank=True, null=True)
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    notes = TextField(blank=True)
    timestamp = DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the object."""
        time = self.timestamp.strftime("%Y-%m-%d-%H:%M:%S")
        user = self.investigator.user.username
        title = '{} - {} - {}'.format(time, self.investigator.name, user)
        return title


class TagDiary(BaseModel):
    """Tag assigned to the Diary"""
    diary = ForeignKey(InvestigatorsDiary, on_delete=CASCADE)
    tag = ForeignKey(Tag, on_delete=PROTECT)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.tag.title, self.diary.title)
        return title


class Item(BaseModel):
    """Item class."""
    category = PositiveIntegerField(
        choices=ITEM_CATEGORIES
    )
    properties = JSONField()

    def __str__(self):
        """String representation of the object."""
        return f"{self.properties['title']}-{self.properties['age']}"


class ItemTag(BaseModel):
    """Tags assigned to the Item."""
    tag = ForeignKey(Tag, on_delete=PROTECT)
    item = ForeignKey(Item, on_delete=CASCADE)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.tag.title, self.item.title)
        return title


class ItemImage(BaseModel):
    """Items image."""
    item = OneToOneField(Item, on_delete=CASCADE)
    image = ImageField(upload_to=renamer)

    def __str__(self):
        """String representation of the object."""
        return self.item.title


class Inventory(BaseModel):
    """Inventory class."""
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    item = ForeignKey(Item, on_delete=CASCADE, null=True, blank=True)
    stock = PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Inventories'

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.item.title, self.investigator.name)
        return title


class Game(BaseModel):
    """Game class."""
    title = CharField(max_length=80)
    description = TextField()
    user = ForeignKey(User, on_delete=CASCADE)
    game_type = CharField(max_length=1, choices=GAME_TYPE)

    def __str__(self):
        """String representation of the object."""
        return self.title


class CampaignInvestigator(BaseModel):
    """Campaign Investigator Relationship"""
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    campaign = ForeignKey(Game, on_delete=CASCADE)
    timestamp = DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {}'.format(self.campaign.title, self.investigator.name)
        return title


class Mania(BaseModel):
    """Manias class."""
    title = CharField(max_length=50)
    description = TextField()

    def __str__(self):
        """String representation of the object."""
        return self.title


class ManiaInvestigator(BaseModel):
    """Manias  Investigator Relationship"""
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    mania = ForeignKey(Mania, on_delete=CASCADE)
    # Undefined limit 999999
    duration = PositiveIntegerField(default=1)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {} - {}'.format(
            self.mania.title, self.investigator.name, self.duration)
        return title


class Phobia(BaseModel):
    """Phobias class."""
    title = CharField(max_length=50)
    description = TextField()

    def __str__(self):
        """String representation of the object."""
        return self.title


class PhobiaInvestigator(BaseModel):
    """Phobias  Investigator Relationship"""
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    phobia = ForeignKey(Phobia, on_delete=CASCADE)
    # Undefined limit 999999
    duration = PositiveIntegerField(default=1)

    def __str__(self):
        """String representation of the object."""
        title = '{} - {} - {}'.format(
            self.phobia.title, self.investigator.name, self.duration)
        return title


class SpellInvestigator(BaseModel):
    """Spell  Investigator Relationship"""
    investigator = ForeignKey(Investigator, on_delete=CASCADE)
    spell = ForeignKey(Spell, on_delete=CASCADE)