from json import loads

from graphene import ObjectType, String, relay
from graphene_django.types import DjangoObjectType

from django.core.serializers import serialize
from django.contrib.auth.models import User

from creator.models import (Investigator, Item, Occupation, Portrait, Skills,
                            Tag, Spell)
from creator.helpers.random_investigator import random_inv


class RandomInvestigatorNode(ObjectType):
    random_investigator = String()

    def resolve_random_investigator(parent, info):
        inv_uuid = random_inv()
        inv = Investigator.objects.get(uuid=inv_uuid)
        res = loads(serialize('json', [inv]))
        return res


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
