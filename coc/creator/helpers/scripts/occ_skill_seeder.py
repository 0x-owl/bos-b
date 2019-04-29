"""Example call of script from /coc/coc location inside container.

python3 creator/helpers/scripts/occ_skill_seeder.py -o Accountant -s
"['Accounting', 'Law', 'Library Use', 'Listen', 'Persuade']"

python3 creator/helpers/scripts/occ_skill_seeder.py -o "
"""
from os import environ, system
from json import dumps, loads

from django.core.wsgi import get_wsgi_application

system("export PYTHONPATH=/coc/coc")  # run this command at the bash
environ.setdefault("DJANGO_SETTINGS_MODULE", "coc.settings")
apps = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'creator'
]
environ.setdefault("INSTALLED_APPS", str(apps))
get_wsgi_application()

from creator.models import Occupation, Skills

with open('/coc/coc/creator/helpers/scripts/occupations.json') as occ_file:
    options = occ_file.read()
options = loads(options)
file_path = '/coc/coc/creator/fixtures/occupation_skills/{}.json'
skills = Skills.objects.all()

initial_registry = {
    "model": "creator.OccupationSkills",
    "fields": {
        "occupation": None,
        "skill": None,
        "optional": False,
        "category": None,
        "limit": 0
    }
}


def registry_generator(occupation, skills, optional, category, limit, file_):
    for skill in skills:
        reg = initial_registry
        reg['fields']['skill'] = skill.pk
        reg['fields']['occupation'] = occupation.pk
        reg['fields']['category'] = category
        reg['fields']['limit'] = limit

        file_.write('{},\n'.format(dumps(reg)))
    return True


def determine_category(type_):
    category = '1'
    if type_ == 'professionalt':
        category = '2'
    elif type_ == 'interpersonal':
        category = '3'
    elif type_ == 'combat':
        category = '6'
    elif type_ == 'misc':
        category == '5'
    return category


for occ in options:
    occupation = Occupation.objects.filter(title=occ['occupation']).first()
    with open(file_path.format(occ['occupation']), 'a') as out:
        skills_acquired = []
        for option in occ:
            if option.split('_')[-1] == 'skills':
                if occ[option] != []:
                    type_ = option.split('_')[0]
                    category = determine_category(type_)
                    limit = occ.get('{}_limit'.format(type_), 0)
                    optional = True if type_ != 'profession' else False
                    sks = [sk for sk in skills if sk.title in
                           occ[option]]
                    registry_generator(
                        occupation,
                        sks,
                        optional,
                        category,
                        limit,
                        out
                    )
                    for sk in sks:
                        skills_acquired.append(sk.pk)

        if occ['free_skills_limit'] != 0:
            free_skills = [sk for sk in skills if sk.pk not in skills_acquired]
            category = '4'
            optional = True
            limit = occ['free_skills_limit']
            registry_generator(
                occupation,
                free_skills,
                optional,
                category,
                limit,
                out
            )
