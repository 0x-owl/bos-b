from coc.utils import mutation_flow
from creator.models import (Investigator, Item, Mania, Phobia, Spell, Tag,
                            Weapon)

from market.models import (Content, ContentInvestigator, ContentItem,
                           ContentMania, ContentPhobia, ContentSpell,
                           ContentTag, ContentWeapon)
from market.schema_nodes import (ContentInvestigatorNode, ContentItemNode,
                                 ContentManiaNode, ContentNode,
                                 ContentPhobiaNode, ContentSpellNode,
                                 ContentTagNode, ContentWeaponNode)

from graphene import ClientIDMutation, Field, Int, String
from django.contrib.auth.models import User


class ContentMutation(ClientIDMutation):
    content = Field(ContentNode)

    class Input:
        method = String()
        user = Int()
        uuid = String()
        title = String()
        price = Int()
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
        usr = User.objects.get(pk=input_['user'])
        input_['user'] = usr
        method = input_.pop('method')
        ret = mutation_flow(
            ContentMutation,
            Content,
            method,
            input_,
            'content'
        )
        return ret


class ContentTagMutation(ClientIDMutation):
    content_tag = Field(ContentTagNode)

    class Input:
        method = String()
        uuid = String()
        content = String()
        tag = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        tag = Tag.objects.get(uuid=input_.get('tag', ''))
        content = Content.objects.get(uuid=input_.get('content', ''))
        input_['tag'] = tag
        input_['content'] = content
        method = input_.pop('method')
        ret = mutation_flow(
            ContentTagMutation,
            ContentTag,
            method,
            input_,
            'content_tag'
        )
        return ret


class ContentInvestigatorMutation(ClientIDMutation):
    content_inv = Field(ContentInvestigatorNode)

    class Input:
        method = String()
        uuid = String()
        content = String()
        inv = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        inv = Investigator.objects.get(uuid=input_.get('inv', ''))
        content = Content.objects.get(uuid=input_.get('content', ''))
        input_['inv'] = inv
        input_['content'] = content
        method = input_.pop('method')
        ret = mutation_flow(
            ContentInvestigatorMutation,
            ContentInvestigator,
            method,
            input_,
            'content_inv'
        )
        return ret


class ContentItemMutation(ClientIDMutation):
    content_item = Field(ContentItemNode)

    class Input:
        method = String()
        uuid = String()
        content = String()
        item = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        item = Item.objects.get(uuid=input_.get('item', ''))
        content = Content.objects.get(uuid=input_.get('content', ''))
        input_['item'] = item
        input_['content'] = content
        method = input_.pop('method')
        ret = mutation_flow(
            ContentItemMutation,
            ContentItem,
            method,
            input_,
            'content_item'
        )
        return ret


class ContentSpellMutation(ClientIDMutation):
    content_spell = Field(ContentSpellNode)

    class Input:
        method = String()
        uuid = String()
        content = String()
        spell = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        spell = Spell.objects.get(uuid=input_.get('spell', ''))
        content = Content.objects.get(uuid=input_.get('content', ''))
        input_['spell'] = spell
        input_['content'] = content
        method = input_.pop('method')
        ret = mutation_flow(
            ContentSpellMutation,
            ContentSpell,
            method,
            input_,
            'content_spell'
        )
        return ret


class ContentWeaponMutation(ClientIDMutation):
    content_weapon = Field(ContentWeaponNode)

    class Input:
        method = String()
        uuid = String()
        content = String()
        weapon = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        weapon = Weapon.objects.get(uuid=input_.get('weapon', ''))
        content = Content.objects.get(uuid=input_.get('content', ''))
        input_['weapon'] = weapon
        input_['content'] = content
        method = input_.pop('method')
        ret = mutation_flow(
            ContentWeaponMutation,
            ContentWeapon,
            method,
            input_,
            'content_weapon'
        )
        return ret


class ContentManiaMutation(ClientIDMutation):
    content_mania = Field(ContentManiaNode)

    class Input:
        method = String()
        uuid = String()
        content = String()
        mania = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        mania = Mania.objects.get(uuid=input_.get('mania', ''))
        content = Content.objects.get(uuid=input_.get('content', ''))
        input_['mania'] = mania
        input_['content'] = content
        method = input_.pop('method')
        ret = mutation_flow(
            ContentManiaMutation,
            ContentMania,
            method,
            input_,
            'content_mania'
        )
        return ret


class ContentPhobiaMutation(ClientIDMutation):
    content_phobia = Field(ContentPhobiaNode)

    class Input:
        method = String()
        uuid = String()
        content = String()
        phobia = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        phobia = Phobia.objects.get(uuid=input_.get('phobia', ''))
        content = Content.objects.get(uuid=input_.get('content', ''))
        input_['phobia'] = phobia
        input_['content'] = content
        method = input_.pop('method')
        ret = mutation_flow(
            ContentPhobiaMutation,
            ContentPhobia,
            method,
            input_,
            'content_phobia'
        )
        return ret
