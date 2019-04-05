from graphene import ClientIDMutation, Field, Int, String, relay
from creator.models import Portrait, Tag
from django.contrib.auth.models import User

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'username': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'uuid': ['exact'],
            'user': ['exact'],
            'user__username': ['exact', 'istartswith'],
            'user__id': ['exact']
        }
        interfaces = (relay.Node, )


class CreateTag(ClientIDMutation):
    tag = Field(TagNode)

    class Input:
        title = String()
        user = Int()

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        arguments = kwargs.get('input')
        tag = Tag(
            title=arguments.get('title'),
            user=User.objects.get(pk=arguments.get('user'))
        )
        tag.save()
        return CreateTag(tag=tag)


class UpdateDeleteTag(ClientIDMutation):
    tag = Field(TagNode)

    class Input:
        title = String()
        uuid = String()
        method = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        uuid = kwargs.get('input').get('uuid', '')
        if uuid != '':
            tag = Tag.objects.get(uuid=uuid)
            if tag is not None and kwargs.get('input').get('method') != 'DEL':
                tag.title = kwargs.get('input').get('title')
                tag.save()
                ret = UpdateDeleteTag(tag=tag)
            else:
                tag.delete()
                ret = "Delete"
            return ret


class PortraitNode(DjangoObjectType):
    class Meta:
        model = Portrait
        filter_fields = {
            'uuid': ['exact']
        }
        interfaces = (relay.Node, )


class Query(object):
    all_tags = DjangoFilterConnectionField(TagNode)
    tag = relay.Node.Field(TagNode)

    all_user = DjangoFilterConnectionField(UserNode)
    user = relay.Node.Field(UserNode)

    all_portraits = DjangoFilterConnectionField(PortraitNode)
    portrait = relay.Node.Field(PortraitNode)


class Mutation(object):
    new_tag = CreateTag.Field()
    update_delete_tag = UpdateDeleteTag.Field()
