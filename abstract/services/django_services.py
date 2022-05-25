from abc import ABC, abstractmethod

from abstract.interfaces.base_interface import BaseRepository
from abstract.services.base_classes import BaseServices


class AuthorBasicServices(BaseServices):

    def __init__(self, author_repository: BaseRepository):
        self.author_repository = author_repository

    def list(self):
        authors = self.author_repository.get_all()
        return authors

    def retrieve(self, pk: int):
        author = self.author_repository.get(pk)
        return author

    def create(self, params: dict):
        author = self.author_repository.create(
            params
        )
        return author

    def update(self, pk: int, update_params: dict):
        author = self.author_repository.update(pk, update_params)
        return author

    def destroy(self, pk: int):
        self.author_repository.delete(pk)


class BookBasicServices(BaseServices):

    def __init__(self, book_repository: BaseRepository):
        self.book_repository = book_repository

    def retrieve(self, pk: int):
        book = self.book_repository.get(pk)
        return book

    def list(self):
        books = self.book_repository.get_all()
        return books

    def create(self, params: dict):
        book = self.book_repository.create(params)
        return book

    def update(self, pk: int, update_params: dict):
        book = self.book_repository.update(pk, update_params)
        return book

    def destroy(self, pk: int):
        self.book_repository.delete(pk)


class Services:

    def __init__(
        self,
        book_services: BaseServices,
        author_services: BaseServices,
    ):
        self.book_services = book_services
        self.author_services = author_services

    def list_all_books_from_author(self, author_id: int):
        books = self.book_services.book_repository.filter_by(author_id=author_id)
        if not books:
            raise ValueError(f'Theres no book for the author {author_id}')

        return books

    def publish_book(self, author_id: int, book_data):
        author = self.author_services.retrieve(author_id)
        book_data['author_id'] = author.id
        book = self.book_services.create(book_data)
        return book





