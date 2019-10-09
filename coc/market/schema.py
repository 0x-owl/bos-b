from market.schema_nodes import (ContentInvestigatorNode, ContentItemNode,
                                 ContentManiaNode, ContentNode,
                                 ContentPhobiaNode, ContentSpellNode,
                                 ContentTagNode, ContentWeaponNode)
from market.schema_mutations import (ContentInvestigatorMutation,
                                     ContentItemMutation, ContentManiaMutation,
                                     ContentMutation, ContentPhobiaMutation,
                                     ContentSpellMutation, ContentTagMutation,
                                     ContentWeaponMutation)

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

    all_content_items = DjangoFilterConnectionField(ContentItemNode)
    content_item = relay.Node.Field(ContentItemNode)

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
    content_inv_mutate = ContentInvestigatorMutation.Field()
    content_item_mutate = ContentItemMutation.Field()
    content_spell_mutate = ContentSpellMutation.Field()
    content_weapon_mutate = ContentWeaponMutation.Field()
    content_mania_mutate = ContentManiaMutation.Field()
    content_phobia_mutate = ContentPhobiaMutation.Field()
