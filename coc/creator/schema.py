from graphene import ClientIDMutation, Field, Float, Int, String, relay
from creator.models import Portrait, Tag, Item
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


class ItemNode(DjangoObjectType):
    class Meta:
        model = Item
        filter_fields = {
            'uuid': ['exact'],
            'title': ['exact', 'icontains', 'istartswith'],
            'item_type': ['exact'], 
            'price': ['exact', 'gt', 'lt', 'gte', 'lte']
        }
        interfaces = (relay.Node, )


class CreateItem(ClientIDMutation):
    item = Field(ItemNode)

    class Input:
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
        arguments = kwargs.get('input')
        item = Item(
            title=arguments.get('title'),
            item_type=arguments.get('item_type'),
            description=arguments.get('description'),
            price=arguments.get('price')
        )
        item.save()
        return CreateItem(item=item)


class UpdateDeleteItem(ClientIDMutation):
    item = Field(ItemNode)

    class Input:
        uuid = String()
        title = String()
        item_type = Int()
        description = String()
        price = Float()
        method = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        uuid = kwargs.get('input').get('uuid', '')
        if uuid != '':
            item = Item.objects.get(uuid=uuid)
            if item is not None and kwargs.get('input').get('method') != 'DEL':
                item.title = kwargs.get('input').get('title')
                item.item_type = kwargs.get('input').get('item_type')
                item.description = kwargs.get('input').get('description')
                item.price = kwargs.get('input').get('price')
                item.save()
                ret = UpdateDeleteItem(item=item)
            else:
                item.delete()
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

    all_items = DjangoFilterConnectionField(ItemNode)
    item = relay.Node.Field(ItemNode)
    

class Mutation(object):
    new_tag = CreateTag.Field()
    update_delete_tag = UpdateDeleteTag.Field()
    new_item = CreateItem.Field()
    update_delete_item = UpdateDeleteItem.Field()