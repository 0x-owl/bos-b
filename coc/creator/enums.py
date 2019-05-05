from django_enumfield.enum import Enum


class Attribute(Enum):
    """Attribute enum."""
    STR = 1
    DEX = 2
    CON = 3
    POW = 4
    EDU = 5
    INT = 6
    APP = 7
    SIZ = 8


class SpellCategory(Enum):
    """Spell categories enum."""
    BANISHMENT_OR_CONTROL = 1
    BRINGING_FORTH_MONSTERS_AND_GODS = 2
    COMBAT = 3
    COMMUNICATION = 4
    DREAMLANDS = 5
    ENCHANTMENTS = 6
    ENVIRONMENTAL = 7
    EXTENDING_LIFE = 8
    FOLK = 9
    HARMFUL = 10
    INFLUENCE = 11
    MAKING_MONSTERS = 12
    OTHER_SPELLS = 13
    PROTECTION = 14
    RELATING_TO_TIME = 15
    TRANSFORMATION = 16
    TRAVEL_AND_TRANSPORTATION = 17

    class Meta:
        verbose_name_plural = 'Spell categories'


class ItemCategory(Enum):
    """Type of items."""
    MAGIC = 1
    CONSUMABLE = 2
    WEAPON = 3
    TOOL = 4
