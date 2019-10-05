from logging import DEBUG, basicConfig

log = basicConfig(level=DEBUG)


def mutation_flow(mutation, model, method, input_, field):
    """Considers the main flow of action at the mutations this is
    the same for each one of them.
    Arguments:
        mutation -- Mutation class
        model -- Django model to be generated
        method -- CREATE, DELETE OR UPDATE
        input_ -- dictionary that contains all necessary information.
        field -- string that represents the field name of the mutation.
    """
    if method != 'CREATE':
        uuid = input_.pop('uuid')
        mutations = model.objects.filter(
            uuid=uuid)
        if method == 'DELETE':
            mutate = mutations.first()
            mutate.delete()
            ret = mutation(**{field: mutate})
        elif method == 'UPDATE':
            if len(mutations) == 1:
                mutations.update(**input_)
                mutate = mutations.first()
                ret = mutation(**{field: mutate})
            else:
                log.error('Two or more entities have the same uuid!')
                ret = mutation(**{field: mutations.first()})
    else:
        mutate = model(**input_)
        mutate.save()
        ret = mutation(**{field: mutate})

    return ret
