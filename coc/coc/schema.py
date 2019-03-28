from graphene import ObjectType, Schema
from creator.schema import Query as Q


class Query(Q, ObjectType):
    pass


schema = Schema(query=Query)
