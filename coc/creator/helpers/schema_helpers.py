def attribute_resolver(inst, fields, **kwargs):
    """Obtain record from the instance given queriyed through Graph.
    Keyword Arguments:
        inst -- (obj) Django Model class.
        fields -- (dict) Instance attributes mapped to graphene types.
        kwargs -- (dict) query values passed to produce search.
    """
    for attr in fields:
        if kwargs.get(attr) is not None:
            search = {attr: kwargs.get(attr)}
            record = inst.objects.get(**search)
            return record
