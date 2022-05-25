from abc import ABC, abstractmethod


class BaseServices(ABC):

    @abstractmethod
    def list(self):
        """service to list all the elements"""

    @abstractmethod
    def retrieve(self, pk: int):
        """service to get an single instance"""

    @abstractmethod
    def create(self, params: dict):
        """service to create an object"""

    @abstractmethod
    def update(self, pk: int, update_params: dict):
        """service to update an element"""

    @abstractmethod
    def destroy(self, pk: int):
        """Service to destroy an element"""
