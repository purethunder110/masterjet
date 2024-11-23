import graphene
from .utils import UserType
from .User import UserModel
import logging

log=logging.getLogger(__name__)


class UserQueries(graphene.ObjectType):

    #QUERIES

    User = graphene.Field(
        UserType,
        id=graphene.ID(required=True,description="user id for filter"),
        description="User Instance"
    )

    #RESOLVERS

    def resolve_User(self,info,**data):
        pk=data.get("id")
        username=graphene.Node.get_node_from_global_id(info,global_id=pk)
        user=UserModel.objects.filter(username=username).first()
        return user
