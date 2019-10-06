from json import loads
from creator.models import (Investigator, Item, Mania, ManiaInvestigator,
                            Occupation, Phobia, PhobiaInvestigator, Portrait,
                            Skills, Spell, Tag, Weapon)

from graphene import ObjectType, String, relay
from graphene_django.types import DjangoObjectType

from django.core.serializers import serialize
from django.contrib.auth.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'username': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'uuid': ['exact'],
            'user': ['exact'],
            'user__username': ['exact', 'icontains', 'istartswith'],
            'user__id': ['exact']
        }
        interfaces = (relay.Node, )


class ItemNode(DjangoObjectType):
    class Meta:
        model = Item
        filter_fields = {
            'uuid': ['exact'],
            'title': ['exact', 'icontains', 'istartswith'],
            'item_type': ['exact'],
            'price': ['exact', 'gt', 'lt', 'gte', 'lte']
        }
        interfaces = (relay.Node, )


class WeaponNode(DjangoObjectType):
    class Meta:
        model = Weapon
        filter_fields = {
            'uuid': ['exact'],
            'title': ['exact', 'icontains', 'istartswith'],
            'item_type': ['exact'],
            'price': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'damage': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class OccupationNode(DjangoObjectType):
    class Meta:
        model = Occupation
        filter_fields = {
            'uuid': ['exact'],
            'user': ['exact'],
            'user__username': ['exact', 'istartswith'],
            'user__id': ['exact'],
            'title': ['exact', 'icontains', 'istartswith'],
            'suggested_contacts': ['icontains'],
            'credit_rating_min': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'credit_rating_max': ['exact', 'gt', 'lt', 'gte', 'lte']
        }
        interfaces = (relay.Node, )


class SkillNode(DjangoObjectType):
    class Meta:
        model = Skills
        filter_fields = {
            'uuid': ['exact'],
            'user': ['exact'],
            'user__username': ['exact', 'istartswith'],
            'user__id': ['exact'],
            'title': ['exact', 'icontains', 'istartswith'],
            'default_value': ['exact'],
        }
        interfaces = (relay.Node, )


class InvestigatorNode(DjangoObjectType):
    class Meta:
        model = Investigator
        filter_fields = {
            'uuid': ['exact'],
            'user': ['exact'],
            'user__username': ['exact', 'istartswith'],
            'user__id': ['exact'],
            'sex': ['exact'],
            'age': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'occupation': ['exact'],
        }
        interfaces = (relay.Node, )


class PortraitNode(DjangoObjectType):
    class Meta:
        model = Portrait
        filter_fields = {
            'uuid': ['exact']
        }
        interfaces = (relay.Node, )


class SpellNode(DjangoObjectType):
    class Meta:
        model = Spell
        filter_fields = {
            'uuid': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
            'cost': ['exact', 'gt', 'lt', 'gte', 'lte'],
            'casting_time': ['exact', 'gt', 'lt', 'gte', 'lte']
        }
        interfaces = (relay.Node, )


class ManiaNode(DjangoObjectType):
    class Meta:
        model = Mania
        filter_fields = {
            'uuid': ['exact'],
            'title': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )


class ManiaInvNode(DjangoObjectType):
    class Meta:
        model = ManiaInvestigator
        filter_fields = {
            'uuid': ['exact'],
            'investigator': ['exact'],
            'mania': ['exact'],
            'duration': ['exact', 'gt', 'lt', 'gte', 'lte']
        }
        interfaces = (relay.Node, )


class PhobiaNode(DjangoObjectType):
    class Meta:
        model = Phobia
        filter_fields = {
            'uuid': ['exact'],
            'title': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )


class PhobiaInvNode(DjangoObjectType):
    class Meta:
        model = PhobiaInvestigator
        filter_fields = {
            'uuid': ['exact'],
            'investigator': ['exact'],
            'phobia': ['exact'],
            'duration': ['exact', 'gt', 'lt', 'gte', 'lte']
        }
        interfaces = (relay.Node, )
