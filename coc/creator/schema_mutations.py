from graphene import (ClientIDMutation, Field, Float, Int, ObjectType, String,
                      relay)
from django.contrib.auth.models import User

from creator.models import (Investigator, Item, Occupation, Portrait, Skills,
                            Tag)
from creator.schema_nodes import (InvestigatorNode, ItemNode, OccupationNode,
                                  SkillNode, TagNode, UserNode)


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
        input_ = kwargs.get('input')
        title = input_.get('title')
        user = input_.get('user')
        tag = Tag(
            title=title,
            user=User.objects.get(pk=user)
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
        input_ = kwargs.get('input')
        uuid = input_.get('uuid', '')
        method = input_.get('method')
        title = input_.get('title')
        if uuid != '':
            tag = Tag.objects.get(uuid=uuid)
            if tag is not None and method != 'DEL':
                tag.title = title
                tag.save()
                ret = UpdateDeleteTag(tag=tag)
            else:
                tag.delete()
                ret = "Delete"
            return ret


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
        input_ = kwargs.get('input')
        title = input_.get('title')
        item_type = input_.get('item_type')
        description = input_.get('description')
        price = input_.get('price')
        item = Item(
            title=title,
            item_type=item_type,
            description=description,
            price=price
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
        input_ = kwargs.get('input')
        uuid = input_.get('uuid', '')
        method = input_.get('method')
        title = input_.get('title')
        item_type = input_.get('item_type')
        description = input_.get('description')
        price = input_.get('price')
        if uuid != '':
            item = Item.objects.get(uuid=uuid)
            if item is not None and method != 'DEL':
                item.title = title
                item.item_type = item_type
                item.description = description
                item.price = price
                item.save()
                ret = UpdateDeleteItem(item=item)
            else:
                item.delete()
                ret = "Delete"
            return ret


class CreateOccupation(ClientIDMutation):
    occupation = Field(OccupationNode)

    class Input:
        user = Int()
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
        user = input_.get('user')
        title = input_.get('title')
        description = input_.get('description')
        suggested_contacts = input_.get('suggested_contacts')
        credit_rating_min = input_.get('credit_rating_min')
        credit_rating_max = input_.get('credit_rating_max')
        occupation = Occupation(
            user=User.objects.get(pk=user),
            title=title,
            description=description,
            suggested_contacts=suggested_contacts,
            credit_rating_min=credit_rating_min,
            credit_rating_max=credit_rating_max
        )
        occupation.save()
        return CreateOccupation(occupation=occupation)


class UpdateDeleteOccupation(ClientIDMutation):
    occupation = Field(OccupationNode)

    class Input:
        uuid = String()
        title = String()
        description = String()
        suggested_contacts = String()
        credit_rating_min = Float()
        credit_rating_max = Float()
        method = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        input_ = kwargs.get('input')
        uuid = input_.get('uuid', '')
        method = input_.get('method')
        title = input_.get('title')
        description = input_.get('description')
        suggested_contacts = input_.get('suggested_contacts')
        credit_rating_min = input_.get('credit_rating_min')
        credit_rating_max = input_.get('credit_rating_max')
        if uuid != '':
            occupation = Occupation.objects.get(uuid=uuid)
            if occupation is not None and method != 'DEL':
                occupation.title = title
                occupation.description = description
                occupation.suggested_contacts = suggested_contacts
                occupation.credit_rating_min = credit_rating_min
                occupation.credit_rating_max = credit_rating_max
                occupation.save()
                ret = UpdateDeleteOccupation(occupation=occupation)
            else:
                occupation.delete()
                ret = "Delete"
            return ret



class CreateSkill(ClientIDMutation):
    skill = Field(SkillNode)

    class Input:
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
        usr = User.objects.get(pk=input_['user'])
        input_['user'] = usr
        skill = Skills(**input_)
        skill.save()
        return CreateSkill(skill=skill)


class UpdateDeleteSkill(ClientIDMutation):
    skill = Field(SkillNode)

    class Input:
        uuid = String()
        user = Int()
        title = String()
        description = String()
        default_value = Int()
        method = String()

    @classmethod
    def mutate(cls, *args, **kwargs):
        input_ = kwargs.get('input')
        uuid = input_.get('uuid', '')
        title = input_.get('title')
        description = input_.get('description')
        default_value = input_.get('default_value')
        method = input_.get('method')
        if uuid != '':
            skill = Skills.objects.get(uuid=uuid)
            if skill is not None and method != 'DEL':
                skill.title = title
                skill.description = description
                skill.default_value = default_value
                skill.save()
                ret = UpdateDeleteSkill(skill=skill)
            else:
                skill.delete()
                ret = "Delete"
            return ret


class CreateInvestigator(ClientIDMutation):
    investigator = Field(InvestigatorNode)

    class Input:
        user = Int()
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

    @classmethod
    def mutate(cls, *args, **kwargs):
        """Generates mutation which is an instance of the Node class which
        results in a instance of our model.
        Arguments:
            input -- (dict) dictionary that has the keys corresponding to the
            Input class (title, user).
        """
        input_ = kwargs.get('input')
        occ = Occupation.objects.get(pk=input_['occupation'])
        usr = User.objects.get(pk=input_['user'])
        input_['user'] = usr
        input_['occupation'] = occ
        investigator = Investigator(**input_)
        investigator.save()
        return CreateInvestigator(investigator=investigator)


class UpdateDeleteInvestigator(ClientIDMutation):
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

    @classmethod
    def mutate(cls, *args, **kwargs):
        input_ = kwargs.get('input')
        uuid = input_.get('uuid', '')
        name = input_.get('name')
        player = input_.get('player')
        sex = input_.get('sex')
        residence = input_.get('residence')
        birthplace = input_.get('birthplace')
        age = input_.get('age')
        occupation = input_.get('occupation')
        ideologies = input_.get('ideologies')
        description = input_.get('description')
        traits = input_.get('traits')
        injure_scars = input_.get('injure_scars')
        significant_people = input_.get('significant_people')
        meaningful_locations = input_.get('meaningful_locations')
        treasured_possessions = input_.get('treasured_possessions')
        encounters_with_strange_entities = input_.get(
            'encounters_with_strange_entities'
        )
        method = input_.get('method')
        if uuid != '':
            investigator = Investigator.objects.get(uuid=uuid)
            if investigator is not None and method != 'DEL':
                investigator.name = name
                investigator.player = player
                investigator.sex = sex
                investigator.residence = residence
                investigator.birthplace = birthplace
                investigator.age = age
                investigator.occupation = Occupation.objects.get(pk=occupation)
                investigator.ideologies = ideologies
                investigator.description = description
                investigator.traits = traits
                investigator.injure_scars = injure_scars
                investigator.significant_people = significant_people
                investigator.meaningful_locations = meaningful_locations
                investigator.treasured_possessions = treasured_possessions
                investigator.encounters_with_strange_entities =\
                    encounters_with_strange_entities
                investigator.save()
                ret = UpdateDeleteInvestigator(investigator=investigator)
            else:
                investigator.delete()
                ret = "Delete"
            return ret
