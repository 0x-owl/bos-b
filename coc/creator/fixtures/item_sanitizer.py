from json import dumps, loads


def fixture_creator(skill):
    skill = {
        "model": "creator.Skills",
        "fields": {
            "title": skill['title'],
            "year": "1920's",
            "base_value": skill.get('value', 0),
            "description": skill.get('description', ""),
            "uncommon": False,
            "sub_skills": skill.get('sub_skills', '')
        }
    }
    return skill

with open('coc/creator/fixtures/core/skills.json', 'r') as fix:
    skills = fix.read()

skills = loads(skills)[0]['fields']['skills']
curated = []

for skill in skills:
    skills[skill]['title'] = skill
    curated.append(
        fixture_creator(skills[skill])
    )

with open('skills_curated.json', 'w') as fixture:
    fixture.write(dumps(curated))
    
