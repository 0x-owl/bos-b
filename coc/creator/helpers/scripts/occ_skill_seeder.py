"""Example call of script from /coc/coc location inside container.

python3 creator/helpers/scripts/occ_skill_seeder.py -o Accountant -s
"['Accounting', 'Law', 'Library Use', 'Listen', 'Persuade']"

python3 creator/helpers/scripts/occ_skill_seeder.py -o Accountant -s
"['Accounting', 'Law', 'Library Use', 'Listen', 'Persuade']" -op -c "4" -l 2
"""
from os import environ, system
from ast import literal_eval as le
from json import dumps
from argparse import ArgumentParser

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

parser = ArgumentParser()
parser.add_argument('-o', '--occupation', help='name of occupation')
parser.add_argument('-s', '--skills',
                    help='''
List of skills to search, if optional then this list will be
excluded from optionals'''
                    )
parser.add_argument(
    '-op', '--optional', help='Whether if we need a list of optional skills',
    action='store_true'
)
parser.add_argument(
    '-c', '--category', help='Category of the skill (default="1")',
    default="1"
)
parser.add_argument(
    '-l', '--limit', help='Limit of optionals (default=0)',
    default=0
)
args = parser.parse_args()

skills = Skills.objects.all()
occ = Occupation.objects.filter(title=args.occupation).first()
skills_list = le(args.skills)
out = ''
initial_registry = {
        "model": "creator.OccupationSkills",
        "fields": {
            "occupation": None,
            "skill": None,
            "optional": False,
            "category": args.category,
            "limit": args.limit
        }
}

if args.optional:
    sks = [skill for skill in skills if skill.title not in skills_list]
    for skill in sks:
        reg = initial_registry
        reg['fields']['skill'] = skill.pk
        reg['fields']['occupation'] = occ.pk
        reg['fields']['optional'] = True
        out += '{},\n'.format(dumps(reg))

else:
    sks = [skill for skill in skills if skill.title in skills_list]
    for skill in sks:
        reg = initial_registry
        reg['fields']['skill'] = skill.pk
        reg['fields']['occupation'] = occ.pk
        out += '{},\n'.format(dumps(reg))

print(out)
