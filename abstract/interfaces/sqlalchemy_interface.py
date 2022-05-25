from datetime import datetime

from django.conf import settings
from django.http import Http404

from abstract.interfaces.base_interface import (
    BaseRepository
)

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_name = settings.DATABASES.get('default').get('NAME')
engine = create_engine(f'sqlite:////{db_name}', connect_args={"check_same_thread": False})
base = automap_base()
base.prepare(engine, reflect=True)
session = sessionmaker(bind=engine)
session = session(autoflush=True, autocommit=False)
Book = base.classes.abstract_book
Author = base.classes.abstract_author


class SQLAlchemyBookInterface(BaseRepository):
    """initial functionality"""

    def get(self, pk: int):
        book = session.query(Book).get(pk)
        return book

    def get_all(self):
        return session.query(Book).all()

    def filter_by(self, *args, **kwargs):
        filter_params = {}
        for k, v in kwargs.items():
            if not hasattr(Book, k):
                print(f'Model {Book.__name__} has not attribute '
                      f'{k}')
                continue
            filter_params[k] = v
        return session.query(Book).filter_by(**filter_params)

    def create(self, params: dict):
        book = Book(
            name=params.get('name'),
            author_id=params.get('author_id'),
            created_at=datetime.now()
        )
        session.add(book)
        session.commit()
        return book

    def update(self, pk: int, params: dict):
        book = session.query(Book).get(pk)
        book.update(**params)

    def delete(self, pk: int):
        book = session.query(Book).get(pk)
        session.delete(book)

    def save(self, book: Book):
        session.add(book)
        session.commit()
        print('book saved')


class SQLAlchemyAuthorInterface(BaseRepository):
    """extended functionality"""

    def get(self, pk: int):
        author = session.query(Author).get(pk)
        if not author:
            raise Http404
        return author

    def get_all(self):
        return session.query(Author).all()

    def filter_by(self, *args, **kwargs):
        pass

    def create(self, params: dict):
        author = Author(name=params.get('name'),
                        email=params.get('email'),
                        created_at=datetime.now()
                        )
        session.add(author)
        session.commit()
        session.flush()
        return author

    def update(self, pk: int, update_params: dict):
        author = session.query(Author).filter_by(id=pk)
        author.update(update_params)
        session.commit()
        return author.first()

    def delete(self, pk: int):
        session.query(Author).filter(Author.id == pk).delete(
            synchronize_session=False
        )
        session.commit()

    def save(self, author: Author):
        session.add(author)
        session.commit()
        return author



