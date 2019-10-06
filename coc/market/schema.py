from market.schema_nodes import (ContentInvestigatorNode, ContentItemlNode,
                                 ContentManiaNode, ContentNode,
                                 ContentPhobiaNode, ContentSpellNode,
                                 ContentTagNode, ContentWeaponNode)
from market.schema_mutations import (ContentInvestigatorMutation,
                                     ContentMutation, ContentTagMutation)

from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField


class Query(object):
    all_contents = DjangoFilterConnectionField(ContentNode)
    content = relay.Node.Field(ContentNode)

    all_content_tags = DjangoFilterConnectionField(ContentTagNode)
    content_tag = relay.Node.Field(ContentTagNode)

    all_content_investigators = DjangoFilterConnectionField(
        ContentInvestigatorNode)
    content_investigator = relay.Node.Field(ContentInvestigatorNode)

    all_content_items = DjangoFilterConnectionField(ContentItemlNode)
    content_item = relay.Node.Field(ContentItemlNode)

    all_content_manias = DjangoFilterConnectionField(ContentManiaNode)
    content_mania = relay.Node.Field(ContentManiaNode)

    all_content_phobias = DjangoFilterConnectionField(ContentPhobiaNode)
    content_phobia = relay.Node.Field(ContentPhobiaNode)

    all_content_spells = DjangoFilterConnectionField(ContentSpellNode)
    content_spell = relay.Node.Field(ContentSpellNode)

    all_content_weapons = DjangoFilterConnectionField(ContentWeaponNode)
    content_weapon = relay.Node.Field(ContentWeaponNode)


class Mutation(object):
    content_mutate = ContentMutation.Field()
    content_tag_mutate = ContentTagMutation.Field()
    content_investigator_mutate = ContentInvestigatorMutation.Field()
