from graphene import ObjectType, Schema

from market.schema import Mutation as MMarket, Query as QMarket
from creator.schema import Mutation as MCreator, Query as QCreator


class Query(QCreator, QMarket, ObjectType):
    pass


class Mutation(MCreator, MMarket, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
