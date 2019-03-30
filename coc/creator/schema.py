from graphene import Field, List
from graphene_django.types import DjangoObjectType

from creator.models import Item, Tag
from creator.constants import TAG_FIELDS
from creator.helpers.schema_helpers import attribute_resolver


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
        **TAG_FIELDS
    )

    def resolve_all_items(self, info, **kwargs):
        """Obtain all records from Item model."""
        return Item.objects.all()

    def resolve_all_tags(self, info, **kwargs):
        """Obtain all records from Tag model."""
        return Tag.objects.all()

    def resolve_tag(self, info, **kwargs):
        """Obtain record that matches specific query over fields."""
        return attribute_resolver(Tag, TAG_FIELDS, kwargs)
