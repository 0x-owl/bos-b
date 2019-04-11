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
