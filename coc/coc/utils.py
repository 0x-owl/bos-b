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
    method = method.lower().strip()
    if method != 'create':
        uuid = input_.get('uuid')
        assert uuid is not None, "Mutations require a UUID"
        mutations = model.objects.filter(uuid=uuid)
        if method == 'delete':
            mutate = mutations.first()
            mutate.delete()
            # Mitigates Graphql "GraphQLError: Cannot return null for non-nullable field"
            mutate.uuid = uuid
            return mutation(**{field: mutate})
    
        if method == 'update':
            del input_['uuid']
            mutations.update(**input_)
            mutate = mutations.first()

            return mutation(**{field: mutate})
    else: 
        mutate = model(**input_) 
        mutate.save()
        return mutation(**{field: mutate})
