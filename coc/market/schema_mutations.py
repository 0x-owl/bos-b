from copy import copy
from coc.utils import mutation_flow
from creator.models import Tag

from market.models import Content, ContentTag
from market.schema_nodes import ContentNode, ContentTagNode

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
