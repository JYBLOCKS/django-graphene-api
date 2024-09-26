import graphene
from graphene_django import DjangoObjectType

from books.schema import BooksType
from .models import Authors


class AuthorsType(DjangoObjectType):
    class Meta:
        model = Authors
        fields = ('id', 'name', 'last_name', 'books')


class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorsType)
    author = graphene.Field(AuthorsType, id=graphene.ID())

    def resolve_all_authors(root, info):
        return Authors.objects.all()

    def resolve_author(root, info, id):
        return Authors.objects.get(pk=id)


class AddAuthorMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        last_name = graphene.String()

    author = graphene.Field(AuthorsType)

    @classmethod
    def mutate(cls, root, info, name, last_name, books):
        author = Authors()
        author.name = name
        author.last_name = last_name
        author.books = books
        author.save()
        return AddAuthorMutation(author=author)


class UpdateAuthorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        last_name = graphene.String()

    author = graphene.Field(AuthorsType)

    @classmethod
    def mutate(cls, root, info, id, name, last_name, books):
        author = Authors.objects.get(pk=id)
        author.name = name
        author.last_name = last_name
        author.books = books
        author.save()
        return UpdateAuthorMutation(author=author)


class DeleteAuthorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, id):
        author = Authors.objects.get(pk=id)
        author.delete()
        return DeleteAuthorMutation(message="delete author with id: " + id)


class Mutation(graphene.ObjectType):
    add_author = AddAuthorMutation.Field()
    update_author = UpdateAuthorMutation.Field()
    delete_author = DeleteAuthorMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
