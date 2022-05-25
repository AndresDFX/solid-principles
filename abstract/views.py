from rest_framework.decorators import action
from rest_framework.response import Response

from abstract.interfaces.django_interface import DjangoBookInterface, DjangoAuthorInterface
from abstract.interfaces.sqlalchemy_interface import SQLAlchemyBookInterface, SQLAlchemyAuthorInterface
from abstract.models import Author, Book
from rest_framework.viewsets import ViewSet
from rest_framework.serializers import PrimaryKeyRelatedField, ModelSerializer
from abstract.services.django_services import (
    BookBasicServices,
    AuthorBasicServices,
    Services
)


class AuthorViewSet(ViewSet):

    services = Services(
        author_services=AuthorBasicServices(
            author_repository=DjangoAuthorInterface()
        ),
        book_services=BookBasicServices(
            book_repository=DjangoAuthorInterface()
        ),
    )

    class AuthorSerializer(ModelSerializer):
        class Meta:
            model = Author
            fields = '__all__'

    class BookSerializer(ModelSerializer):

        class Meta:
            model = Book
            fields = ['id', 'name', 'created_at']

    author_serializer_class = AuthorSerializer
    book_serializer_class = BookSerializer

    def list(self, request):
        authors = self.services.author_services.list()
        serializer = self.author_serializer_class(authors, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = self.services.author_services.retrieve(pk)
        serializer = self.author_serializer_class(obj)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        author = self.services.author_services.create(data)
        serializer = self.author_serializer_class(author)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        data = request.data
        author = self.services.author_services.update(pk=pk, update_params=data)
        serializer = self.author_serializer_class(author)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            self.services.author_services.destroy(pk)
            return Response({'msg': 'success'})
        except Exception as e:
            print(e)
            return Response({'error': 'error'})

    @action(detail=True, methods=['GET'])
    def books(self, request, pk=None):
        books = self.services.list_all_books_from_author(author_id=pk)
        books_serialize = self.book_serializer_class(books, many=True)
        return Response(books_serialize.data)

    @action(detail=True, methods=['POST'])
    def publish(self, request, pk=None):
        book_data = request.data
        book = self.services.publish_book(author_id=pk, book_data=book_data)
        book_response = self.book_serializer_class(book)
        return Response(book_response.data)




