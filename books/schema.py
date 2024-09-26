import graphene
from graphene_django import DjangoObjectType
from .models import Books


class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ('id', 'title', 'excerpt', 'authors')


class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)
    book = graphene.Field(BooksType, id=graphene.ID())

    def resolve_all_books(root, info):
        return Books.objects.all()

    def resolve_book(root, info, id):
        return Books.objects.get(pk=id)


class AddBookMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        excerpt = graphene.String()

    book = graphene.Field(BooksType)

    @classmethod
    def mutate(cls, root, info, title, excerpt):
        book = Books()
        book.title = title
        book.excerpt = excerpt
        book.save()
        return AddBookMutation(book=book)


class UpdateBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        excerpt = graphene.String()

    book = graphene.Field(BooksType)

    @classmethod
    def mutate(cls, root, info, id, title, excerpt):
        book = Books.objects.get(pk=id)
        book.title = title
        book.excerpt = excerpt
        book.save()
        return UpdateBookMutation(book=book)


class DeleteBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, id):
        book = Books.objects.get(pk=id)
        book.delete()
        return DeleteBookMutation(message="delete book with id: " + id)


class Mutation(graphene.ObjectType):
    add_book = AddBookMutation.Field()
    update_book = UpdateBookMutation.Field()
    delete_book = DeleteBookMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
