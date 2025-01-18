from graphene_django import DjangoObjectType
from .User import UserModel
import graphene


class UserType(DjangoObjectType):
    class Meta:
        model = UserModel
        fields = ["userid", "email", "first_name", "username", "is_staff"]
        # filter_fields=["userid"]
        interfaces = (graphene.relay.Node,)
