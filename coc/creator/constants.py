from graphene import Int, String

GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)

GAME_TYPE = (
    ('1', 'One-Shot'),
    ('2', 'Campaign')
)

ERA = (
    ('1920', '1920'),
    ('modern', 'Modern'),
    ('WWII', 'WorldWar 2')
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
    "/uploads/basics/img/silouette_male.png",
    "/uploads/basics/img/silouette_female.png"
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

GATE_CREATION_AND_TRAVEL_COSTS = [
    {
        "miles": 100,
        "approximate_light_years": 0,
        "magic_points": "1",
        "pow": "5"

    },
    {
        "miles": 1000,
        "approximate_light_years": 0,
        "magic_points": 2,
        "pow": 10
    },
    {
        "miles": 10000,
        "approximate_light_years": 0,
        "magic_points": 3,
        "pow": 15
    },
    {
        "miles": 100000,
        "approximate_light_years": 0,
        "magic_points": 4,
        "pow": 20
    },
    {
        "miles": 1000000,
        "approximate_light_years": 0,
        "magic_points": 5,
        "pow": 25
    },
    {
        "miles": 10000000,
        "approximate_light_years": 0,
        "magic_points": 6,
        "pow": 30
    },
    {
        "miles": 100000000,
        "approximate_light_years": 0,
        "magic_points": 7,
        "pow": 35
    },
    {
        "miles": 1000000000,
        "approximate_light_years": 0,
        "magic_points": 8,
        "pow": 40
    },
    {
        "miles": 10000000000,
        "approximate_light_years": 0,
        "magic_points": 9,
        "pow": 45
    },
    {
        "miles": 100000000000,
        "approximate_light_years": 0,
        "magic_points": 10,
        "pow": 50
    },
    {
        "miles": 1000000000000,
        "approximate_light_years": 0,
        "magic_points": 11,
        "pow": 55
    },
    {
        "miles": 0,
        "approximate_light_years": 0.5,
        "magic_points": 12,
        "pow": 60
    },
    {
        "miles": 0,
        "approximate_light_years": 5,
        "magic_points": 13,
        "pow": 65
    },
    {
        "miles": 0,
        "approximate_light_years": 50,
        "magic_points": 14,
        "pow": 70
    },
    {
        "miles": 0,
        "approximate_light_years": 500,
        "magic_points": 15,
        "pow": 75
    },
    {
        "miles": 0,
        "approximate_light_years": 5000,
        "magic_points": 16,
        "pow": 80
    },
    {
        "miles": 0,
        "approximate_light_years": 50000,
        "magic_points": 17,
        "pow": 85
    },
    {
        "miles": 0,
        "approximate_light_years": 500000,
        "magic_points": 18,
        "pow": 90
    },
    {
        "miles": 0,
        "approximate_light_years": 5000000,
        "magic_points": 19,
        "pow": 95
    },
    {
        "miles": 0,
        "approximate_light_years": 50000000,
        "magic_points": 20,
        "pow": 100
    }
]

GATE_LOCATIONS_AND_DISTANCES = [
    {
        "distance_from_boston": "Providence",
        "approximate_miles": 40,
        "approximate_light_years": 0,
        "pow": 5,
        "magic_points": 1
    },
    {
        "distance_from_boston": "Peoria",
        "approximate_miles": 1000,
        "approximate_light_years": 0,
        "pow": 10,
        "magic_points": 2
    },
    {
        "distance_from_boston": "Portland (Australia)",
        "approximate_miles": 10000,
        "approximate_light_years": 0,
        "pow": 15,
        "magic_points": 3
    },
    {
        "distance_from_boston": "Empty Space",
        "approximate_miles": 100000,
        "approximate_light_years": 0,
        "pow": 20,
        "magic_points": 4
    },
    {
        "distance_from_boston": "Moon",
        "approximate_miles": 230000,
        "approximate_light_years": 0,
        "pow": 25,
        "magic_points": 5
    },
    {
        "distance_from_boston": "Mercury",
        "approximate_miles": 140000000,
        "approximate_light_years": 0,
        "pow": 40,
        "magic_points": 8
    },
    {
        "distance_from_boston": "Venus",
        "approximate_miles": 160000000,
        "approximate_light_years": 0,
        "pow": 40,
        "magic_points": 8
    },
    {
        "distance_from_boston": "Mars",
        "approximate_miles": 250000000,
        "approximate_light_years": 0,
        "pow": 40,
        "magic_points": 8
    },
    {
        "distance_from_boston": "Jupiter",
        "approximate_miles": 600000000,
        "approximate_light_years": 0,
        "pow": 40,
        "magic_points": 8
    },
    {
        "distance_from_boston": "Jupiter",
        "approximate_miles": 600000000,
        "approximate_light_years": 0,
        "pow": 40,
        "magic_points": 8
    },
    {
        "distance_from_boston": "Saturn",
        "approximate_miles": 1000000000,
        "approximate_light_years": 0,
        "pow": 40,
        "magic_points": 8
    },
    {
        "distance_from_boston": "Uranus",
        "approximate_miles": 1900000000,
        "approximate_light_years": 0,
        "pow": 45,
        "magic_points": 9
    },
    {
        "distance_from_boston": "Neptune",
        "approximate_miles": 2800000000,
        "approximate_light_years": 0,
        "pow": 45,
        "magic_points": 9
    },
    {
        "distance_from_boston": "Yuggoth (Pluto)",
        "approximate_miles": 4600000000,
        "approximate_light_years": 0,
        "pow": 45,
        "magic_points": 9
    },
    {
        "distance_from_boston": "Oort Cloud",
        "approximate_miles": 9000000000,
        "approximate_light_years": 0,
        "pow": 45,
        "magic_points": 9
    },
    {
        "distance_from_boston": "Proxima Centauri",
        "approximate_miles": 0,
        "approximate_light_years": 4.3,
        "pow": 65,
        "magic_points": 13
    },
    {
        "distance_from_boston": "Sirius",
        "approximate_miles": 0,
        "approximate_light_years": 8.3,
        "pow": 70,
        "magic_points": 14
    },
    {
        "distance_from_boston": "Fomalhaut",
        "approximate_miles": 0,
        "approximate_light_years": 22,
        "pow": 70,
        "magic_points": 14
    },
    {
        "distance_from_boston": "Vega",
        "approximate_miles": 0,
        "approximate_light_years": 26,
        "pow": 70,
        "magic_points": 14
    },
    {
        "distance_from_boston": "Aldebaran",
        "approximate_miles": 0,
        "approximate_light_years": 50,
        "pow": 70,
        "magic_points": 14
    },
    {
        "distance_from_boston": "Celaeno",
        "approximate_miles": 0,
        "approximate_light_years": 400,
        "pow": 75,
        "magic_points": 15
    },
    {
        "distance_from_boston": "Far side of the Milky Way",
        "approximate_miles": 0,
        "approximate_light_years": 70000,
        "pow": 90,
        "magic_points": 18
    },
    {
        "distance_from_boston": "Galaxy M31",
        "approximate_miles": 0,
        "approximate_light_years": 2800000,
        "pow": 95,
        "magic_points": 19
    },
    {
        "distance_from_boston": "Azathoth",
        "approximate_miles": 0,
        "approximate_light_years": 10000000000,
        "pow": 105,
        "magic_points": 23
    },
    {
        "distance_from_boston": "Distant Quasar",
        "approximate_miles": 0,
        "approximate_light_years": 15000000000,
        "pow": 105,
        "magic_points": 23
    },
    {
        "distance_from_boston": "1 astronomical unit",
        "approximate_miles": 93000000,
        "approximate_light_years": 0,
        "pow": 35,
        "magic_points": 7
    },
    {
        "distance_from_boston": "1 light year",
        "approximate_miles": 5900000000000,
        "approximate_light_years": 0,
        "pow": 60,
        "magic_points": 12
    },
    {
        "distance_from_boston": "1 parsec",
        "approximate_miles": 0,
        "approximate_light_years": 3.26,
        "pow": 65,
        "magic_points": 13
    }
]