from json import loads

from creator.models import (CampaignInvestigator, Game, Inventory,
                            Investigator,
                            InvestigatorsDiary,
                            InvestigatorTags, Item, Mania, ManiaInvestigator,
                            Occupation, Phobia, PhobiaInvestigator, Portrait,
                            Skills, Spell, Tag)

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
            'category': ['exact'],
        }
        interfaces = (relay.Node, )


class OccupationNode(DjangoObjectType):
    class Meta:
        model = Occupation
        filter_fields = {
            'uuid': ['exact'],
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
            'title': ['exact', 'icontains', 'istartswith'],
            'uuid': ['exact'],
            'year': ['exact']
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


class CampaignInvNode(DjangoObjectType):
    class Meta:
        model = CampaignInvestigator
        filter_fields = {
            'uuid': ['exact'],
            'campaign': ['exact'],
            'investigator': ['exact']
        }
        interfaces = (relay.Node, )


class InventoryInvNode(DjangoObjectType):
    class Meta:
        model = Inventory
        filter_fields = {
            'uuid': ['exact'],
            'investigator': ['exact'],
            'item': ['exact'],
            'stock': ['exact', 'gt', 'lt', 'gte', 'lte']
        }
        interfaces = (relay.Node, )


class DiaryInvNode(DjangoObjectType):
    class Meta:
        model = InvestigatorsDiary
        filter_fields = {
            'uuid': ['exact'],
            'investigator': ['exact'],
            'title': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )


class TagInvNode(DjangoObjectType):
    class Meta:
        model = InvestigatorTags
        filter_fields = {
            'uuid': ['exact'],
            'tag': ['exact'],
            'investigator': ['exact']
        }
        interfaces = (relay.Node, )


class GameNode(DjangoObjectType):
    class Meta:
        model = Game
        filter_fields = {
            'uuid': ['exact'],
            'user': ['exact'],
            'user__username': ['exact', 'istartswith'],
            'user__id': ['exact'],
            'title': ['exact', 'icontains', 'istartswith'],
            'game_type': ['exact']
        }
        interfaces = (relay.Node, )
