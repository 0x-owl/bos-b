import django
from os import environ, path
from json import dumps, loads

from django.core.wsgi import get_wsgi_application
environ.setdefault("DJANGO_SETTINGS_MODULE", "coc.settings")
APPS = [
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'creator'
]
django.setup()
environ.setdefault("INSTALLED_APPS", str(APPS))
app = get_wsgi_application()


from creator.models import Item
from creator.constants import ITEM_CATEGORIES
from json import dumps


def fixture_creator(item):
    item = {
        "model": "creator.Item",
        "fields": {
            "category": item.category,
            "properties": {
                "title": item.properties['title'],
                "description": item.properties['description'],
                "price": item.properties['price'],
                "age": item.properties['age']
            }
        }
    }
    return item

categories = dict(ITEM_CATEGORIES)
items = Item.objects.all()

for category in categories:
    items = list(Item.objects.filter(category=category))
    if items:
        with open(f'coc/creator/fixtures/items/items_{categories[category].lower()}.json', 'w') as fixture:
            fixture.write('[\n')
            last_item = items.pop(-1)
            for item in items:
                item_dump = fixture_creator(item)
                fixture.write(f"{dumps(item_dump)},\n")
            last_item_dump = fixture_creator(last_item)
            fixture.write(f"{dumps(last_item_dump)}\n")
            fixture.write(']')

    
