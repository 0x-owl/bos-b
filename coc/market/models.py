from uuid import uuid4

from django.db.models import (CASCADE, CharField, ForeignKey, Model, PROTECT,
                              PositiveIntegerField, TextField, UUIDField)
from django.contrib.auth.models import User

from creator.models import (Investigator, Item, Mania, Occupation, Phobia,
                            Spell, Tag, Weapon)


# Create your models here.
class Content(Model):
    """Content class."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    title = CharField(max_length=100)
    description = TextField()
    user = ForeignKey(User, on_delete=CASCADE)
    price = PositiveIntegerField(default=0)

    def __str__(self):
        """String representation of the object."""
        return f'{self.title}'


class ContentTag(Model):
    """Class that associates Content with a User."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    content = ForeignKey(Content, on_delete=CASCADE)
    tag = ForeignKey(Tag, on_delete=PROTECT)

    def __str__(self):
        """String representation of the object."""
        return f'{self.tag.title}-{self.content.title}'


class ContentUser(Model):
    """Class that associates Content with a User."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    content = ForeignKey(Content, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=PROTECT)

    def __str__(self):
        """String representation of the object."""
        return f'{self.user.username}-{self.content.title}'


class ContentInvestigator(Model):
    """Class that associates Content with a Investigator."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    content = ForeignKey(Content, on_delete=CASCADE)
    inv = ForeignKey(Investigator, on_delete=PROTECT)

    def __str__(self):
        """String representation of the object."""
        return f'{self.inv.name}-{self.content.title}'


class ContentSpell(Model):
    """class that associates content with a spell."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    content = ForeignKey(Content, on_delete=CASCADE)
    spell = ForeignKey(Spell, on_delete=PROTECT)

    def __str__(self):
        """string representation of the object."""
        return f'{self.spell.name}-{self.content.title}'


class ContentItem(Model):
    """Class that associates content with an Item."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    content = ForeignKey(Content, on_delete=CASCADE)
    item = ForeignKey(Item, on_delete=PROTECT)

    def __str__(self):
        """string representation of the object."""
        return f'{self.item.title}-{self.content.title}'


class ContentOccupation(Model):
    """Class that associates content with an Occupation."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    content = ForeignKey(Content, on_delete=CASCADE)
    occ = ForeignKey(Occupation, on_delete=PROTECT)

    def __str__(self):
        """string representation of the object."""
        return f'{self.occ.title}-{self.content.title}'


class ContentPhobia(Model):
    """Class that associates content with a Phobia."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    content = ForeignKey(Content, on_delete=CASCADE)
    phobia = ForeignKey(Phobia, on_delete=PROTECT)

    def __str__(self):
        """string representation of the object."""
        return f'{self.phobia.title}-{self.content.title}'


class ContentMania(Model):
    """Class that associates content with a Mania."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    content = ForeignKey(Content, on_delete=CASCADE)
    mania = ForeignKey(Mania, on_delete=PROTECT)

    def __str__(self):
        """string representation of the object."""
        return f'{self.mania.title}-{self.content.title}'


class ContentWeapon(Model):
    """Class that associates content with a Weapon."""
    uuid = UUIDField(unique=True, default=uuid4, editable=False)
    content = ForeignKey(Content, on_delete=CASCADE)
    weapon = ForeignKey(Weapon, on_delete=PROTECT)

    def __str__(self):
        """string representation of the object."""
        return f'{self.weapon.title}-{self.content.title}'
