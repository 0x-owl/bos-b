from graphene import List, Field, Int, String
from graphene_django.types import DjangoObjectType

from creator.models import Item, Tag


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class Query(object):
    all_items = List(ItemType)
    all_tags = List(TagType)
    tag = Field(
        TagType,
        pk=Int(),
        title=String(),
        uuid=String()
    )

    def resolve_all_items(self, info, **kwargs):
        return Item.objects.all()

    def resolve_all_tags(self, info, **kwargs):
        return Tag.objects.all()

    def resolve_tag(self, info, **kwargs):
        pk = kwargs.get('pk')
        uuid = kwargs.get('uuid')
        title = kwargs.get('title')
        ret = None

        if pk is not None:
            tag = Tag.objects.get(pk=pk)
            ret = tag

        if uuid is not None:
            tag = Tag.objects.get(uuid=uuid)
            ret = tag

        if title is not None:
            tag = Tag.objects.get(title=title)
            ret = tag

        return ret
