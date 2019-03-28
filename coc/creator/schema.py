from graphene import List
from graphene_django.types import DjangoObjectType

from creator.models import Item


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class Query(object):
    all_items = List(ItemType)

    def resolve_all_items(self, info, **kwargs):
        return Item.objects.all()
