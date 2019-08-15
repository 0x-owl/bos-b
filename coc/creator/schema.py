from graphene import Field, relay
from graphene_django.filter import DjangoFilterConnectionField

from creator.schema_nodes import (InvestigatorNode, ItemNode, OccupationNode,
                                  PortraitNode, RandomInvestigatorNode,
                                  SkillNode, SpellNode, TagNode, UserNode)
from creator.schema_mutations import (CreateInvestigator, CreateItem,
                                      CreateOccupation, CreateSkill, CreateTag,
                                      SpellMutation, UpdateDeleteInvestigator,
                                      UpdateDeleteItem, UpdateDeleteOccupation,
                                      UpdateDeleteSkill, UpdateDeleteTag)


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

    all_investigators = DjangoFilterConnectionField(InvestigatorNode)
    investigator = relay.Node.Field(InvestigatorNode)

    all_spells = DjangoFilterConnectionField(SpellNode)
    spell = relay.Node.Field(SpellNode)

    random_investigator = Field(RandomInvestigatorNode)

    def resolve_random_investigator(self, info):
        return info


class Mutation(object):
    new_tag = CreateTag.Field()
    update_delete_tag = UpdateDeleteTag.Field()
    new_item = CreateItem.Field()
    update_delete_item = UpdateDeleteItem.Field()
    new_occupation = CreateOccupation.Field()
    update_delete_occupation = UpdateDeleteOccupation.Field()
    new_skill = CreateSkill.Field()
    update_delete_skill = UpdateDeleteSkill.Field()
    new_investigator = CreateInvestigator.Field()
    update_delete_investigator = UpdateDeleteInvestigator.Field()
    spell_mutate = SpellMutation.Field()
