from market.models import Content, ContentTag

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
