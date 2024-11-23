from graphene_django import DjangoObjectType
from .User import UserModel
import graphene

class UserType(DjangoObjectType):
    class Meta:
        model = UserModel
        fields=["userid","email","first_name","username","is_staff"]
        # filter_fields=["userid"]
        interfaces = (graphene.relay.Node,)

    # @classmethod
    # def get_node(cls,info,id):
    #     return UserModel.objects.get(pk=id)
