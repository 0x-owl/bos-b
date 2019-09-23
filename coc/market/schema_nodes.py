from graphene import relay
from graphene_django.types import DjangoObjectType

from market.models import Content


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
