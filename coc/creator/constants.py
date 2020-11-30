from graphene import Int, String

GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)

GAME_TYPE = (
    ('1', 'One-Shot'),
    ('2', 'Campaign')
)

DECADES = (
    ('20', "20's"),
    ('50', "50's"),
    ('90', "90's"),
    ('00', "00's"),
    ('99999', "No end")
)

SKILL_TYPES = (
    ('1', 'Profession'),
    ('2', 'ProfessionAlt'),  # Lawyer -> Law or Other Language
    ('3', 'Interpersonal'),
    ('4', 'Free'),
    ('5', 'Misc'),  # Mostly applies to choices between 3 or 4 general skills
    ('6', 'Combat')
)


TAG_FIELDS = {
    'id': Int(),
    'uuid': String(),
    'title': String(),
    'user_id': Int()
}


SPELL_CATEGORIES = [
    (1, 'BANISHMENT_OR_CONTROL'),
    (2, 'BRINGING_FORTH_MONSTERS_AND_GODS'),
    (3, 'COMBAT'),
    (4, 'COMMUNICATION'),
    (5, 'DREAMLANDS'),
    (6, 'ENCHANTMENTS'),
    (7, 'ENVIRONMENTAL'),
    (8, 'EXTENDING_LIFE'),
    (9, 'FOLK'),
    (10, 'HARMFUL'),
    (11, 'INFLUENCE'),
    (12, 'MAKING_MONSTERS'),
    (13, 'OTHER_SPELLS'),
    (14, 'PROTECTION'),
    (15, 'RELATING_TO_TIME'),
    (16, 'TRANSFORMATION'),
    (17, 'TRAVEL_AND_TRANSPORTATION'),
]

ITEM_CATEGORIES = [
    (1, 'MAGIC'),
    (2, 'CONSUMABLE'),
    (3, 'WEAPON'),
    (4, 'TOOL')
]
