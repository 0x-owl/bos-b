from json import dumps, loads
from os import listdir


def fixture_creator(item):
    item = item['fields']
    properties = item['properties']
    properties['price'] = properties.get('price', 0.0)
    if isinstance(properties['price'], str):
        if ' - ' in properties['price']:
            max_price = float(properties['price'].split(' - ')[1].strip())
            base_price = float(properties['price'].split(' - ')[0].strip())
        elif '+' in properties['price']:
            max_price = None
            base_price = float(properties['price'].replace('+', ''))
    else:
        max_price = 0
        base_price = properties['price']

    era_item = properties.get('era', '1920')
    era = 'modern' if ',' in era_item else era_item.lower()
    
    item_fix = {
        "model": "creator.Item",
        "fields": {
            "title": properties['title'],
            "description": properties.get('description', ''),
            "era": era,
            "base_price": base_price,
            "max_price": max_price,
            "category": item['category'],
        }
    }
    del properties['era']
    del properties['price']
    del properties['title']
    del properties['description']
    item_fix['fields']['properties'] = properties
    return item_fix


def weapon_fixture_creator(item):
    item = item['fields']
    properties = item['properties']

    # determine era or eras
    rare = 'rare' in properties['era'].lower()
    eras = properties['era'].split(', ')
    if len(eras) > 2 and 'Rare' not in eras:
        costs = properties['cost_20s_modern'].replace('$','').split('/')
        costs = [float(cost) if cost != '-' else None for cost in costs]  
        
    else:

    era = 'modern' if 'modern' in properties['era'].lower() else '1920'
    
    # determine if two versions
    current_prices = properties['cost_20s_modern'].split('/')


    properties['price'] = properties.get('price', 0.0)
    if '+' in properties['price']:
        max_price = None
        base_price = float(properties['price'].replace('+', ''))
    else:
        max_price = 0
        base_price = properties['price']

    era_item = properties.get('era', '1920')
    era = 'modern' if 'Modern' in era_item else era_item.lower()
    
    item_fix = {
        "model": "creator.Item",
        "fields": {
            "title": properties['title'],
            "description": properties.get('description', ''),
            "base_price": base_price,
            "max_price": max_price,
            "category": item['category'],
        }
    }
    del properties['era']
    del properties['price']
    del properties['title']
    del properties['description']
    item_fix['fields']['properties'] = properties
    return item_fix



fixtures = listdir('coc/creator/fixtures/items')

for fixture in fixtures:
    
    path = f'coc/creator/fixtures/items/{fixture}'
    curated = []
    with open(path, 'r') as fix:
        items = fix.read()
        items = loads(items)
        if 'weapons' in fixture:
            for item in items:
                curated.append(
                    weapon_fixture_creator((item))
                )
        else:
            for item in items:
                curated.append(
                    fixture_creator(item)
                )


    fixture_name = fixture.split('.')[0]
    with open(
        f'coc/creator/fixtures/items/{fixture_name}_curated.json', 'w') as fix_c:
        fix_c.write(
            dumps(curated)
        )
    
