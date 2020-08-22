import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from .models import UrlModel

"""
Class to manage GraphQL schema
"""

# Create a GraphQL type for the url model
class UrlType(DjangoObjectType):
    class Meta:
        model = UrlModel

class QueryType(graphene.ObjectType):
    urls = graphene.List(UrlType)

    def resolve_url(self, info, **kwargs):
        url = kwargs.get('url')
        if url is not None:
            return UrlModel.objects.get(pk=url)
        return None

    def resolve_urls(self, info, **kwargs):
        return UrlModel.objects.all()

# Create mutations for url
class CreateUrl(graphene.Mutation):
    url = graphene.Field(UrlType)
    status = graphene.Boolean()
    class Arguments:
        url =  graphene.String()

    @staticmethod
    def mutate(root, info, url):
        status = True
        url_instance = UrlModel(url=url)
        url_instance.save()
        return CreateUrl(status=status, url=url_instance)

# Class to hold graphql mutations
class Mutation(graphene.ObjectType):
    create_url = CreateUrl.Field()

schema = graphene.Schema(query=QueryType, mutation=Mutation)