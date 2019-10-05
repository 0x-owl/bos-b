from coc.utils import mutation_flow

from creator.models import (Investigator, Item, Mania, Occupation, Phobia,
                            Portrait, Skills, Spell, Tag, Weapon)
from creator.schema_nodes import (InvestigatorNode, ItemNode, ManiaNode,
                                  OccupationNode, PhobiaNode, SkillNode,
                                  SpellNode, TagNode, UserNode, WeaponNode)

from graphene import (ClientIDMutation, Field, Float, Int, ObjectType, String,
                      relay)
from django.contrib.auth.models import User


class TagMutation(ClientIDMutation):
    tag = Field(TagNode)

    class Input:
        method = String()
        user = Int()
        uuid = String()
        title = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        usr = User.objects.get(pk=input_['user'])
        input_['user'] = usr
        method = input_.pop('method')
        ret = mutation_flow(
            TagMutation,
            Tag,
            method,
            input_,
            'tag'
        )
        return ret


class ItemMutation(ClientIDMutation):
    item = Field(ItemNode)

    class Input:
        method = String()
        user = Int()
        uuid = String()
        title = String()
        item_type = Int()
        description = String()
        price = Float()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        usr = User.objects.get(pk=input_['user'])
        input_['user'] = usr
        method = input_.pop('method')
        ret = mutation_flow(
            ItemMutation,
            Item,
            method,
            input_,
            'item'
        )
        return ret


class OccupationMutation(ClientIDMutation):
    occupation = Field(OccupationNode)

    class Input:
        method = String()
        user = Int()
        uuid = String()
        title = String()
        description = String()
        suggested_contacts = String()
        credit_rating_min = Float()
        credit_rating_max = Float()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        usr = User.objects.get(pk=input_['user'])
        input_['user'] = usr
        method = input_.pop('method')
        ret = mutation_flow(
            OccupationMutation,
            Occupation,
            method,
            input_,
            'occupation'
        )

        return ret


class SkillMutation(ClientIDMutation):
    skill = Field(SkillNode)

    class Input:
        method = String()
        uuid = String()
        user = Int()
        title = String()
        description = String()
        default_value = Int()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        input_['user'] = User.objects.filter(pk=input_.get('user')).first()
        method = input_.pop('method')
        ret = mutation_flow(
            SkillMutation,
            Skills,
            method,
            input_,
            'skill'
        )
        return ret

class InvestigatorMutation(ClientIDMutation):
    investigator = Field(InvestigatorNode)

    class Input:
        uuid = String()
        name = String()
        player = String()
        sex = String()
        residence = String()
        birthplace = String()
        age = Int()
        occupation = Int()
        ideologies = String()
        description = String()
        traits = String()
        injure_scars = String()
        significant_people = String()
        meaningful_locations = String()
        treasured_possessions = String()
        encounters_with_strange_entities = String()
        method = String()
        user = Int()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        method = input_.pop('method')
        input_['user'] = User.objects.filter(pk=input_.get('user')).first()
        input_['occupation'] = Occupation.objects.filter(
            pk=input_.get('occupation')
        ).first()
        ret = mutation_flow(
            InvestigatorMutation,
            Investigator,
            method,
            input_,
            'investigator'
        )

        return ret


class SpellMutation(ClientIDMutation):
    spell = Field(SpellNode)

    class Input:
        method = String()
        uuid = String()
        name = String()
        alternative_names = String()
        description = String()
        deeper_magic = String()
        notes = String()
        cost = String()
        casting_time = String()
        user = Int()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        usr = User.objects.get(pk=input_['user'])
        input_['user'] = usr
        method = input_.pop('method')
        ret = mutation_flow(
            SpellMutation,
            Spell,
            method,
            input_,
            'spell'
        )
        return ret


class WeaponMutation(ClientIDMutation):
    weapon = Field(WeaponNode)

    class Input:
        method = String()
        user = Int()
        uuid = String()
        title = String()
        item_type = Int()
        description = String()
        price = Float()
        damage = String()
        base_range = String()
        uses_per_round = String()
        mal_function = Int()


    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        usr = User.objects.get(pk=input_['user'])
        input_['user'] = usr
        method = input_.pop('method')
        ret = mutation_flow(
            WeaponMutation,
            Weapon,
            method,
            input_,
            'weapon'
        )
        return ret


class ManiaMutation(ClientIDMutation):
    mania = Field(ManiaNode)

    class Input:
        method = String()
        uuid = String()
        title = String()
        description = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        method = input_.pop('method')
        ret = mutation_flow(
            ManiaMutation,
            Mania,
            method,
            input_,
            'mania'
        )
        return ret


class PhobiaMutation(ClientIDMutation):
    phobia = Field(PhobiaNode)

    class Input:
        method = String()
        uuid = String()
        title = String()
        description = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        method = input_.pop('method')
        ret = mutation_flow(
            PhobiaMutation,
            Phobia,
            method,
            input_,
            'phobia'
        )
        return ret

