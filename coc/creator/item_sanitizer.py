from coc.creator.models import Item
from json import dumps

items = Item.objects.all()


def fixture_creator(item):
    age = item.description.splite(' - ')[-1]
    item = {
        "category": item.category,
        "properties": {
            "title": item.title,
            "description": item.description,
            "price": item.price,
            "age": age
        }
    }
    return item


with open('items.json', 'w') as fixture:
    fixture.write('[\n')
    last_item = items.pop(-1)
    for item in items:
        item_dump = fixture_creator(item)
        fixture.write(f"{dumps(item_dump)},\n")
    last_item_dump = fixture_creator(last_item)
    fixture.write(f"{dumps(last_item_dump)}\n")
    fixture.write(']')

    
