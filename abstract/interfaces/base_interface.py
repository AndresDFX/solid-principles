from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    def get(self, pk: int):
        """Get an instance"""

    @abstractmethod
    def get_all(self):
        """List all the instances"""

    @abstractmethod
    def filter_by(self, *args, **kwargs):
        """Filter instances based on params"""

    @abstractmethod
    def create(self, params: dict):
        """create an instance object"""

    @abstractmethod
    def update(self, pk: int, params: dict):
        """update an instance object"""

    @abstractmethod
    def delete(self, pk: int):
        """delete an instance object"""

    @abstractmethod
    def save(self, obj: object):
        """save an instance object"""

