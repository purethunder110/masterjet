import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="HI")

schema=graphene.Schema(query=Query)