from graphene import Field, relay
from graphene_django.filter import DjangoFilterConnectionField

from creator.models import Investigator
from creator.schema_nodes import (InvestigatorNode, ItemNode, OccupationNode,
                                  PortraitNode, SkillNode, SpellNode, TagNode,
                                  UserNode)
from creator.schema_mutations import (InvestigatorMutation, ItemMutation,
                                      OccupationMutation, SkillMutation,
                                      SpellMutation, TagMutation)
from creator.helpers.random_investigator import random_inv


class Query(object):
    all_tags = DjangoFilterConnectionField(TagNode)
    tag = relay.Node.Field(TagNode)

    all_user = DjangoFilterConnectionField(UserNode)
    user = relay.Node.Field(UserNode)

    all_portraits = DjangoFilterConnectionField(PortraitNode)
    portrait = relay.Node.Field(PortraitNode)

    all_items = DjangoFilterConnectionField(ItemNode)
    item = relay.Node.Field(ItemNode)

    all_occupations = DjangoFilterConnectionField(OccupationNode)
    occupation = relay.Node.Field(OccupationNode)

    all_skills = DjangoFilterConnectionField(SkillNode)
    skill = relay.Node.Field(SkillNode)

    investigator = relay.Node.Field(InvestigatorNode)
    all_investigators = DjangoFilterConnectionField(InvestigatorNode)

    all_spells = DjangoFilterConnectionField(SpellNode)
    spell = relay.Node.Field(SpellNode)

    random_investigator = Field(InvestigatorNode)

    def resolve_random_investigator(self, info):
        inv_uuid = random_inv()
        inv = Investigator.objects.get(uuid=inv_uuid)
        return inv



class Mutation(object):
    tag_mutate = TagMutation.Field()
    item_mutate = ItemMutation.Field()
    occupation_mutate = OccupationMutation.Field()
    skill_mutate = SkillMutation.Field()
    investigator_mutate = InvestigatorMutation.Field()
    spell_mutate = SpellMutation.Field()
