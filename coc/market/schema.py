from market.schema_nodes import ContentNode, ContentTagNode
from market.schema_mutations import ContentMutation, ContentTagMutation

from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField


class Query(object):
    all_contents = DjangoFilterConnectionField(ContentNode)
    content = relay.Node.Field(ContentNode)

    all_content_tags = DjangoFilterConnectionField(ContentTagNode)
    content_tag = relay.Node.Field(ContentTagNode)


class Mutation(object):
    content_mutate = ContentMutation.Field()
    content_tag_mutate = ContentTagMutation.Field()
