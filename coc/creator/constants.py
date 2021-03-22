from graphene import Int, String

GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)

GAME_TYPE = (
    ('1', 'One-Shot'),
    ('2', 'Campaign')
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
    (3, 'WEAPONS'),
    (4, 'AMMO'),
    (5, 'TOOL'),
    (6, 'VEHICLE'),
    (7, 'MISC')
]

SILOUETTES = [
    "/uploads/basics/img/silouette_male.jpg",
    "/uploads/basics/img/silouette_female.jpg"
]

CREDIT_RATING = {
    "1920": {
        "penniless": {
            "min": 0,
            "max": 0,
            "cash": 0.5,
            "assets": 0,
            "spending_level": 0.5,
        },
        "poor": {
            "min": 1,
            "max": 9,
            "cash": 1,
            "assets": 10,
            "spending_level": 2
        },
        "average": {
            "min": 10,
            "max": 49,
            "cash": 2,
            "assets": 50,
            "spending_level": 10
        },
        "wealthy": {
            "min": 50,
            "max": 89,
            "cash": 5,
            "assets": 500,
            "spending_level": 50
        },
        "rich": {
            "min": 90,
            "max": 98,
            "cash": 20,
            "assets": 2000,
            "spending_level": 250
        },
        "super_rich": {
            "min": 99,
            "max": 100,
            "cash": 50000,
            "assets": 5000000,
            "spending_level": 5000
        }
    },
    "modern": {
        "penniless": {
            "min": 0,
            "max": 0,
            "cash": 10,
            "assets": 0,
            "spending_level": 10
        },
        "poor": {
            "min": 1,
            "max": 9,
            "cash": 20,
            "assets": 200,
            "spending_level": 40
        },
        "average": {
            "min": 10,
            "max": 49,
            "cash": 40,
            "assets": 1000,
            "spending_level": 200
        },
        "wealthy": {
            "min": 50,
            "max": 89,
            "cash": 100,
            "assets": 10000,
            "spending_level": 1000
        },
        "rich": {
            "min": 90,
            "max": 98,
            "cash": 400,
            "assets": 40000,
            "spending_level": 5000
        },
        "super_rich": {
            "min": 99,
            "max": 100,
            "cash": 1000000,
            "assets": 100000000,
            "spending_level": 100000
        }
    }
}
