from graphene import relay
from creator.models import Tag
from django.contrib.auth.models import User

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'id': ['exact'],
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
            'user__username': ['exact', 'istartswith'],
            'id': ['exact']
        }
        interfaces = (relay.Node, )


class Query(object):
    all_tags = DjangoFilterConnectionField(TagNode)
    tag = relay.Node.Field(TagNode)

    all_user = DjangoFilterConnectionField(UserNode)
    user = relay.Node.Field(UserNode)
