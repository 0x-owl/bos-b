from coc.utils import mutation_flow

from creator.models import (CampaignInvestigator, Game, Inventory,
                            Investigator, InvestigatorAttribute,
                            InvestigatorsDiary, InvestigatorSkills,
                            InvestigatorTags, Item, Mania, ManiaInvestigator,
                            Occupation, Phobia, PhobiaInvestigator, Portrait,
                            Skills, Spell, Tag, Weapon)

from creator.schema_nodes import (AttrInvNode, CampaignInvNode, DiaryInvNode,
                                  GameNode, InventoryInvNode, InvestigatorNode,
                                  ItemNode, ManiaNode, ManiaInvNode,
                                  OccupationNode, PhobiaNode, PhobiaInvNode,
                                  SkillNode, SkillInvNode, SpellNode, TagNode,
                                  TagInvNode, UserNode, WeaponNode, UserNode)

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


class ManiaInvMutation(ClientIDMutation):
    maniaInv = Field(ManiaInvNode)

    class Input:
        method = String()
        uuid = String()
        investigator = String()
        mania = String()
        duration = Int()

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
        input_['investigator'] = Investigator.objects.filter(
            uuid=input_.get('investigator')).first()
        input_['mania'] = Mania.objects.filter(
            uuid=input_.get('mania')
        ).first()
        ret = mutation_flow(
            ManiaInvMutation,
            ManiaInvestigator,
            method,
            input_,
            'maniaInv'
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


class PhobiaInvMutation(ClientIDMutation):
    phobiaInv = Field(PhobiaInvNode)

    class Input:
        method = String()
        uuid = String()
        investigator = String()
        phobia = String()
        duration = Int()

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
        input_['investigator'] = Investigator.objects.filter(
            uuid=input_.get('investigator')).first()
        input_['phobia'] = Phobia.objects.filter(
            uuid=input_.get('phobia')
        ).first()
        ret = mutation_flow(
            PhobiaInvMutation,
            PhobiaInvestigator,
            method,
            input_,
            'phobiaInv'
        )
        return ret


class CampaignInvMutation(ClientIDMutation):
    campaign_inv = Field(CampaignInvNode)

    class Input:
        method = String()
        uuid = String()
        investigator = String()
        campaign = String()

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
        input_['investigator'] = Investigator.objects.filter(
            uuid=input_.get('investigator')).first()
        input_['campaign'] = Game.objects.filter(
            uuid=input_.get('campaign')).first()
        ret = mutation_flow(
            CampaignInvMutation,
            CampaignInvestigator,
            method,
            input_,
            'campaign_inv'
        )
        return ret


class InventoryInvMutation(ClientIDMutation):
    inventory_inv = Field(InventoryInvNode)

    class Input:
        method = String()
        uuid = String()
        investigator = String()
        item = String()
        stock = Int()

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
        input_['investigator'] = Investigator.objects.filter(
            uuid=input_.get('investigator')).first()
        input_['item'] = Item.objects.filter(
            uuid=input_.get('item')
        ).first()
        ret = mutation_flow(
            InventoryInvMutation,
            Inventory,
            method,
            input_,
            'inventory_inv'
        )

        return ret


class InventoryInvMutation(ClientIDMutation):
    inventory_inv = Field(InventoryInvNode)

    class Input:
        method = String()
        uuid = String()
        investigator = String()
        item = String()
        stock = Int()

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
        input_['investigator'] = Investigator.objects.filter(
            uuid=input_.get('investigator')).first()
        input_['item'] = Item.objects.filter(
            uuid=input_.get('item')
        ).first()
        ret = mutation_flow(
            InventoryInvMutation,
            Inventory,
            method,
            input_,
            'inventory_inv'
        )

        return ret


class DiaryInvMutation(ClientIDMutation):
    diary_inv = Field(DiaryInvNode)

    class Input:
        method = String()
        uuid = String()
        investigator = String()
        title = String()
        notes = String()

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
        input_['investigator'] = Investigator.objects.filter(
            uuid=input_.get('investigator')).first()
        ret = mutation_flow(
            DiaryInvMutation,
            InvestigatorsDiary,
            method,
            input_,
            'diary_inv'
        )

        return ret


class TagInvMutation(ClientIDMutation):
    tag_inv = Field(TagInvNode)

    class Input:
        method = String()
        uuid = String()
        tag = String()
        investigator = String()

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
        input_['investigator'] = Investigator.objects.filter(
            uuid=input_.get('investigator')).first()
        input_['tag'] = Tag.objects.filter(
            uuid=input_.get('tag')
        ).first()
        ret = mutation_flow(
            TagInvMutation,
            InvestigatorTags,
            method,
            input_,
            'tag_inv'
        )

        return ret


class SkillInvMutation(ClientIDMutation):
    skillInv = Field(SkillInvNode)

    class Input:
        method = String()
        uuid = String()
        investigator = String()
        skill = String()
        value = Int()
        category = String()

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
        input_['investigator'] = Investigator.objects.filter(
            uuid=input_.get('investigator')).first()
        input_['skill'] = Skills.objects.filter(
            uuid=input_.get('skill')
        ).first()
        ret = mutation_flow(
            SkillInvMutation,
            InvestigatorSkills,
            method,
            input_,
            'skillInv'
        )

        return ret


class GameMutation(ClientIDMutation):
    game = Field(GameNode)

    class Input:
        method = String()
        user = Int()
        uuid = String()
        title = String()
        description = String()
        game_type = String()

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
            GameMutation,
            Game,
            method,
            input_,
            'game'
        )
        return ret


class AttrInvMutation(ClientIDMutation):
    attrInv = Field(AttrInvNode)

    class Input:
        method = String()
        uuid = String()
        investigator = String()
        attr = Int()
        value = Int()

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
        input_['investigator'] = Investigator.objects.filter(
            uuid=input_.get('investigator')).first()
        ret = mutation_flow(
            AttrInvMutation,
            InvestigatorAttribute,
            method,
            input_,
            'attrInv'
        )

        return ret


class UserMutation(ClientIDMutation):
    user = Field(UserNode)

    class Input:
        method = String()
        username = String()
        first_name = String()
        last_name = String()
        email = String()
        password = String()

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
        ret = None
        # Before update flow
        if method == 'UPDATE':
            users = User.objects.filter(username=input_['username'])
            user = users.first()
            password = user.password
            users.update(**input_)
            user = users.first()
            if password != input_['password']:
                user.set_password(input_['password'])
                user.save()
                user = user
            ret = UserMutation(user=user)
        elif method == 'CREATE':
            user = User(**input_)
            user.set_password(input_['password'])
            user.save()
            ret = UserMutation(user=user)
        elif method == 'DELETE':
            user = User.objects.get(username=input_['username'])
            user.delete()
            ret = UserMutation(user=user)

        return ret
