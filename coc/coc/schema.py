from graphene import ObjectType, Schema
from creator.schema import Query as Q, Mutation as M


class Query(Q, ObjectType):
    pass


class Mutation(M, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
