"""Example call of script from /coc/coc location inside container.

python3 creator/helpers/scripts/occ_skill_seeder.py"
"""
from os import environ, path
from json import dumps, loads

from django.core.wsgi import get_wsgi_application

environ.setdefault("DJANGO_SETTINGS_MODULE", "coc.settings")
APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'creator',
    'market'
]
environ.setdefault("INSTALLED_APPS", str(APPS))
get_wsgi_application()

from creator.models import Occupation, Skills


PATH = '/'.join(path.realpath(__file__).split('/')[:-1])

with open(f'{PATH}/occupations.json') as occ_file:
    OPTIONS = occ_file.read()

OCCUPATIONS = loads(OPTIONS)
FILE_PATH = 'coc/coc/creator/fixtures/occupation_skills/{}.json'
PATH_OUT = '/'.join(path.realpath(__file__).split('/')[:-3])
FILE_OUT_PATH = f'{PATH_OUT}/fixtures/occupation_skills/'
SKILLS = Skills.objects.all()

INITIAL_REGISTRY = {
    "model": "creator.OccupationSkills",
    "fields": {
        "occupation": None,
        "skill": None,
        "optional": False,
        "category": None,
        "limit": 0
    }
}


def registry_generator(
        occupationx: Occupation, skills: Skills, categoryx: str,
        limitx: int, file_: object, optionalx: bool) -> bool:
    """Generates each line of the json for the certain skill."""
    for skill in skills:
        reg = INITIAL_REGISTRY
        reg['fields']['skill'] = skill.pk
        reg['fields']['occupation'] = occupationx.pk
        reg['fields']['category'] = categoryx
        reg['fields']['limit'] = limitx
        reg['fields']['optional'] = optionalx

        reg = dumps(reg)
        file_.write(f'{reg},\n')

    return True


def determine_category(typex: str) -> str:
    """Given a type skill give it a category.
    @param typex (str)
    """
    category_ = '1'
    if typex == 'professionalt':
        category_ = '2'
    elif typex == 'interpersonal':
        category_ = '3'
    elif typex == 'combat':
        category_ = '6'
    elif typex == 'misc':
        category_ = '5'

    return category_


def clean_closing(file_name: str) -> None:
    """Remove last comma and add closing bracket to json file.
    @param file_name: name of the file to be cleaned.
    """
    # Remove last "," from the end line.
    with open(file_name, 'rb+') as clean:
        clean.seek(0, 2)
        size = clean.tell()
        clean.truncate(size - 2)
    with open(file_name, 'a') as clean:
        clean.write(']')


def main():
    """Main function in charge of processing the occupation.json file and
    generate the seeder json files.
    """
    for occ in OCCUPATIONS:
        occupation = Occupation.objects.filter(title=occ['occupation']).first()
        fname = f'{FILE_OUT_PATH}{occ["occupation"]}.json'
        with open(fname, 'a+') as out:
            out.write('[')
            skills_acquired = []
            for option in occ:
                opt_list = option.split('_')
                if opt_list[-1] == 'skills' and occ[option] != []:
                    type_ = opt_list[0]
                    category = determine_category(type_)
                    limit = occ.get('{}_limit'.format(type_), 0)
                    optional = bool(type_ != 'proffesional')
                    skills = [sk for sk in SKILLS if sk.title in occ[option]]

                    if (limit != 0 and optional) or not optional:
                        try:
                            registry_generator(
                                occupationx=occupation,
                                skills=skills,
                                categoryx=category,
                                limitx=limit,
                                file_=out,
                                optionalx=optional
                            )
                        except AttributeError:
                            print(f"Load of occupation {occ} failed")
                        skills_acquired.extend([skill.pk for skill in skills])

            if occ['free_skills_limit'] != 0:
                free_skills = [sk for sk in SKILLS if sk.pk not
                               in skills_acquired]
                category = '4'
                optional = True
                limit = occ['free_skills_limit']
                registry_generator(
                    occupationx=occupation,
                    skills=free_skills,
                    categoryx=category,
                    limitx=limit,
                    file_=out,
                    optionalx=optional
                )
        clean_closing(fname)


if __name__ == '__main__':
    main()
