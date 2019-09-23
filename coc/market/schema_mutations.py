from graphene import (ClientIDMutation, Field, Int, String)
from django.contrib.auth.models import User

from market.models import Content
from market.schema_nodes import ContentNode


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
        if method != 'CREATE':
            content = Content.objects.filter(
                uuid=input_.get('uuid', '')).first()
            if method == 'DELETE':
                content.delete()
                ret = content
            elif method == 'UPDATE':
                content.__dict__.update(input_)
                content.save()
                ret = ContentMutation(content=content)
        else:
            content = Content(**input_)
            content.save()
            ret = ContentMutation(content=content)

        return ret
