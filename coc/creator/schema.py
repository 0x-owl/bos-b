from creator.models import Investigator
from creator.schema_nodes import (InvestigatorNode, ItemNode, ManiaNode,
                                  OccupationNode, PhobiaNode, PortraitNode,
                                  SkillNode, SpellNode, TagNode, UserNode,
                                  WeaponNode)
from creator.schema_mutations import (InvestigatorMutation, ItemMutation,
                                      ManiaMutation, OccupationMutation,
                                      PhobiaMutation, SkillMutation,
                                      SpellMutation, TagMutation, WeaponMutation)
from creator.helpers.random_investigator import random_inv

from graphene import Field, relay
from graphene_django.filter import DjangoFilterConnectionField


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

    all_weapons = DjangoFilterConnectionField(WeaponNode)
    weapon = relay.Node.Field(WeaponNode)

    all_manias = DjangoFilterConnectionField(ManiaNode)
    mania = relay.Node.Field(ManiaNode)

    all_phobias = DjangoFilterConnectionField(PhobiaNode)
    phobia = relay.Node.Field(PhobiaNode)

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
    weapon_mutate = WeaponMutation.Field()
    mania_mutate = ManiaMutation.Field()
    phobia_mutate = PhobiaMutation.Field()
