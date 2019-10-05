from market.models import (Content, ContentInvestigator, ContentItem,
                           ContentMania, ContentOccupation, ContentPhobia,
                           ContentSpell, ContentTag, ContentWeapon)

from graphene import relay
from graphene_django.types import DjangoObjectType


class ContentNode(DjangoObjectType):
    class Meta:
        model = Content
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'uuid': ['exact'],
            'user': ['exact'],
            'user__username': ['exact', 'icontains', 'istartswith'],
            'user__id': ['exact'],
            'price': ['exact', 'gt', 'lt', 'gte', 'lte']
        }
        interfaces = (relay.Node, )


class ContentTagNode(DjangoObjectType):
    class Meta:
        model = ContentTag
        filter_fields = {
            'uuid': ['exact'],
            'content__uuid': ['exact'],
            'tag__uuid': ['exact'],
            'content__title': ['exact', 'icontains', 'istartswith'],
            'tag__title': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )


class ContentInvestigatorNode(DjangoObjectType):
    class Meta:
        model = ContentInvestigator
        filter_fields = {
            'uuid': ['exact'],
            'content__uuid': ['exact'],
            'inv__uuid': ['exact'],
            'content__title': ['exact', 'icontains', 'istartswith'],
            'inv__name': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )


class ContentSpellNode(DjangoObjectType):
    class Meta:
        model = ContentSpell
        filter_fields = {
            'uuid': ['exact'],
            'content__uuid': ['exact'],
            'spell__uuid': ['exact'],
            'content__title': ['exact', 'icontains', 'istartswith'],
            'spell__name': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )


class ContentItemlNode(DjangoObjectType):
    class Meta:
        model = ContentItem
        filter_fields = {
            'uuid': ['exact'],
            'content__uuid': ['exact'],
            'item__uuid': ['exact'],
            'content__title': ['exact', 'icontains', 'istartswith'],
            'item__title': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )


class ContentOccupationNode(DjangoObjectType):
    class Meta:
        model = ContentOccupation
        filter_fields = {
            'uuid': ['exact'],
            'content__uuid': ['exact'],
            'occ__uuid': ['exact'],
            'content__title': ['exact', 'icontains', 'istartswith'],
            'occ__title': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )


class ContentPhobiaNode(DjangoObjectType):
    class Meta:
        model = ContentPhobia
        filter_fields = {
            'uuid': ['exact'],
            'content__uuid': ['exact'],
            'phobia__uuid': ['exact'],
            'content__title': ['exact', 'icontains', 'istartswith'],
            'phobia__title': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )


class ContentManiaNode(DjangoObjectType):
    class Meta:
        model = ContentMania
        filter_fields = {
            'uuid': ['exact'],
            'content__uuid': ['exact'],
            'mania__uuid': ['exact'],
            'content__title': ['exact', 'icontains', 'istartswith'],
            'mania__title': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )


class ContentWeaponNode(DjangoObjectType):
    class Meta:
        model = ContentWeapon
        filter_fields = {
            'uuid': ['exact'],
            'content__uuid': ['exact'],
            'weapon__uuid': ['exact'],
            'content__title': ['exact', 'icontains', 'istartswith'],
            'weapon__title': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )
