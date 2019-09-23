from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from market.schema_nodes import ContentNode
from market.schema_mutations import ContentMutation


class Query(object):
    all_contents = DjangoFilterConnectionField(ContentNode)
    content = relay.Node.Field(ContentNode)


class Mutation(object):
    content_mutate = ContentMutation.Field()
