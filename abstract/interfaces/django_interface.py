from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from django.http import Http404

from abstract.interfaces.base_interface import (
    BaseRepository
)
from abstract.models import Book, Author


class DjangoBookInterface(BaseRepository):
    """initial functionality"""

    def get(self, pk: int) -> Book:
        return Book.objects.get(id=pk)

    def get_all(self) -> QuerySet:
        return Book.objects.all()

    def filter_by(self, *args, **kwargs) -> QuerySet:
        filter_params = {}
        for k, v in kwargs.items():
            if not hasattr(Book, k):
                print(f'Model {Book.__name__} has not attribute '
                      f'{k}')
                continue
            filter_params[k] = v
        result = Book.objects.filter(**filter_params)
        return result

    def create(self, params: dict):
        return Book.objects.create(**params)

    def update(self, pk: int, params: dict):
        Book.objects.filter(id=pk).update(**params)

    def delete(self, pk: int):
        try:
            Book.objects.get(id=pk).delete()
        except ObjectDoesNotExist:
            print(f'Book with id: {pk} does not exists')
            return False

        return True

    def save(self, book: Book):
        book.save()


class DjangoAuthorInterface(BaseRepository):
    """Extended Functionality"""

    def get(self, author_id: str) -> Author:
        try:
            author = Author.objects.get(id=author_id)
        except ObjectDoesNotExist:
            raise Http404
        return author

    def get_all(self) -> QuerySet:
        return Author.objects.all()

    def filter_by(self, author_id: int) -> QuerySet:
        author_books = Book.objects.select_related('author').filter(author_id=author_id)
        return author_books

    def create(self, params: dict):
        return Author.objects.create(**params)

    def update(self, pk: int, params: dict):
        author = Author.objects.get(id=pk)
        for k, v in params.items():
            if hasattr(author, k):
                setattr(author, k, v)
        author.save()
        return author

    def delete(self, author_id: int):
        try:
            Author.objects.get(id=author_id).delete()
        except ObjectDoesNotExist:
            print(f'Author with id: {author_id} does not exists')
            return False

        return True

    def save(self, author: Author):
        author.save()