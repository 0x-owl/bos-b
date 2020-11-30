from datetime import datetime as dt
from random import randint


def obtain_attribute_value(inv, inv_attr, attr, attribute_name):
    """Look for the investigators attribute and return its value.
    Parameters:
        inv -- Investigator class instance.
        inv_attr -- InvestigatorAttribute class.
        attr -- Attribute class.
        attr_name -- name of the attribute e.g. STR, DEX, ...
    """
    attr_value = filter(lambda x: x[0] == attribute_name, attr.items())
    attr_value = attr_value.__next__()[1]
    attr = inv_attr.objects.filter(
        investigator_id=inv.id, attr=attr_value).first()
    return attr


def renamer(instance, filename) -> str:
    """Rename the files to have understandable names.

    Keyword arguments:

    instance -- Model instance.
    filename -- filename of the file being uploaded (wont'be used).
    """
    now = dt.now()
    now = now.strftime('%Y%m%d%H%M%S')
    inst_name = instance.__class__.__name__
    if inst_name == 'Portrait':
        fname_clean = 'portraits/{0}/{1}.jpg'.format(
            instance.investigator.uuid, now)
    else:
        fname_clean = 'items/{0}/{1}.jpg'.format(
            instance.item.uuid, now)
    return fname_clean


def roller_stats(dsix: int = 3) -> int:
    """Roll for stats specifying the amount of d6."""
    stat = sum([randint(1, 6) for _ in range(dsix)])
    if dsix == 2:
        stat += 6
        stat *= 5
    else:
        stat *= 5
    return stat