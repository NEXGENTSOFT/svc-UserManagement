from abc import ABC, abstractmethod
from src.UsersManagement.Domain.Entity.Users import Users
class UsersPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def create_users(self):
        pass

    @abstractmethod
    def update_users(self):
        pass

    @abstractmethod
    def delete_users(self):
        pass


    @abstractmethod
    def login(self):
        pass