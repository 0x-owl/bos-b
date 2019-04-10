"""Example call of script from /coc/coc location inside container.

python3 creator/helpers/scripts/occ_skill_seeder.py -o Accountant -s
"['Accounting', 'Law', 'Library Use', 'Listen', 'Persuade']"
"""
from os import environ
from ast import literal_eval as le
from json import dumps
from pprint import pprint as pp
from argparse import ArgumentParser

from django.core.wsgi import get_wsgi_application

environ.setdefault("PYTHONPATH", "/coc/coc")
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
application = get_wsgi_application()

from creator.models import Occupation, Skills

parser = ArgumentParser()
parser.add_argument('-o', '--occupation', help='name of occupation')
parser.add_argument('-s', '--skills',
                    help='''
List of skills to search, if optional then this list will be
excluded from optionals'''
                    )
parser.add_argument(
    '-op', '--optional', help='whether if we need a list of optional skills',
    action='store_true')
args = parser.parse_args()

skills = Skills.objects.all()
occ = Occupation.objects.filter(title=args.occupation).first()
skills_list = le(args.skills)

seed = []
initial_registry = {
        "model": "creator.OccupationSkills",
        "fields": {
            "occupation": None,
            "skill": None,
            "optional": False
        }
}

if args.optional:
    sks = [skill for skill in skills if skill.title not in skills_list]
    for skill in sks:
        reg = initial_registry
        reg['fields']['skill'] = skill.pk
        reg['fields']['occupation'] = occ.pk
        reg['fields']['optional'] = True
        seed.append(reg)

else:
    sks = [skill for skill in skills if skill.title in skills_list]
    for skill in sks:
        reg = initial_registry
        reg['fields']['skill'] = skill.pk
        reg['fields']['occupation'] = occ.pk
        seed.append(reg)


pp(dumps(seed))
