from graphene import (ClientIDMutation, Field, Float, Int, ObjectType, String,
                      relay)
from django.contrib.auth.models import User

from creator.models import (Investigator, Item, Occupation, Portrait, Skills,
                            Spell, Tag)
from creator.schema_nodes import (InvestigatorNode, ItemNode, OccupationNode,
                                  SkillNode, SpellNode, TagNode, UserNode)


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
        if method != "CREATE":
            tag = Tag.objects.filter(uuid=input_.get('uuid', '')).first()
            if method == 'DELETE':
                tag.delete()
                ret = tag
            elif method == 'UPDATE':
                tag.__dict__.update(input_)
                tag.save()
                ret = TagMutation(tag=tag)
        else:
            tag = Tag(**input_)
            tag.save()
            ret = TagMutation(tag=tag)

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
        if method != "CREATE":
            item = Item.objects.filter(uuid=input_.get('uuid', '')).first()
            if method == 'DELETE':
                item.delete()
                ret = item
            elif method == 'UPDATE':
                item.__dict__.update(input_)
                item.save()
                ret = ItemMutation(item=item)
        else:
            item = Item(**input_)
            item.save()
            ret = ItemMutation(item=item)

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
        if method != "CREATE":
            occupation = Occupation.objects.filter(
                uuid=input_.get('uuid', '')).first()
            if method == 'DELETE':
                occupation.delete()
                ret = occupation
            elif method == 'UPDATE':
                occupation.__dict__.update(input_)
                occupation.save()
                ret = OccupationMutation(occupation=occupation)
        else:
            occupation = Occupation(**input_)
            occupation.save()
            ret = OccupationMutation(occupation=occupation)

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
        if method != "CREATE":
            skill = Skills.objects.filter(uuid=input_.get('uuid', '')).first()
            if method == 'DELETE':
                skill.delete()
                ret = skill
            elif method == 'UPDATE':
                skill.__dict__.update(input_)
                skill.save()
                ret = SkillMutation(skill=skill)
        else:
            skill = Skills(**input_)
            skill.save()
            ret = SkillMutation(skill=skill)

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
        uuid = input_.pop('uuid')
        method = input_.pop('method')
        input_['user'] = User.objects.filter(pk=input_.get('user')).first()
        input_['occupation'] = Occupation.objects.filter(
            pk=input_.get('occupation')
        ).first()
        if method != 'CREATE':
            investigator = Investigator.objects.filter(uuid=uuid).first()
            if method == 'DELETE':
                investigator.delete()
                ret = investigator
            elif method == 'UPDATE':
                investigator.__dict__.update(input_)
                investigator.save()
                ret = InvestigatorMutation(investigator=investigator)
        else:
            investigator = Investigator(**input_)
            investigator.save()
            ret = InvestigatorMutation(investigator=investigator)

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
        if method != "CREATE":
            spell = Spell.objects.filter(uuid=input_.get('uuid', '')).first()
            if method == 'DELETE':
                spell.delete()
                ret = spell
            elif method == 'UPDATE':
                spell.__dict__.update(input_)
                spell.save()
                ret = SpellMutation(spell=spell)
        else:
            spell = Spell(**input_)
            spell.save()
            ret = SpellMutation(spell=spell)

        return ret
