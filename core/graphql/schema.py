# from graphene_federation import build_schema
from core.user.query import UserQueries
from graphene import Schema, Node


# QUERY SCHEMA
class QuerySchema(UserQueries): ...


# schema=build_schema(QuerySchema)

schema = Schema(query=QuerySchema)
