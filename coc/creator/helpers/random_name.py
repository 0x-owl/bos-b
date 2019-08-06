from simplejson import load
from random import choice


def random_names(gender, decade, amount_of_names, amount_of_surnames):
    """Randoms name generator.
    Parameters:
        gender - Male or female sex
        decade - Decade of the 20 'or 00'
        amount_of_names - Number of first names
        amount_of_surnames - Number of surnames
    """
    with open('first_names.json', 'r') as first_names:
        first_names = load(first_names)

    with open('last_names.json', 'r') as last_names:
        last_names = load(last_names)

    names_list = []
    surnames_list = [surname['last_name'] for surname in last_names]

    random_surname = choice(surnames_list)

    if amount_of_surnames == 2:
        random_surname = random_surname + ' ' + choice(surnames_list)

    for name in first_names:
        if name['decade'] == decade and name['gender'] == gender:
            names_list.append(name['first_name'])

    random_name = choice(names_list)

    if amount_of_names == 2:
        random_name = random_name + ' ' + choice(names_list)

    random_name = random_name + ' ' + random_surname
    return random_name
