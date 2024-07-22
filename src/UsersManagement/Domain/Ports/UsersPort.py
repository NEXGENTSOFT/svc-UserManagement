from abc import ABC, abstractmethod
from src.UsersManagement.Domain.Entity.Users import Users
class UsersPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_users(self, uuid: str):
        pass

    @abstractmethod
    def create_users(self, user: Users):
        pass

    @abstractmethod
    def update_users(self, uuid: str, newPassword: str, password: str, username: str):
        pass

    @abstractmethod
    def delete_users(self, uuid: str, password: str):
        pass


    @abstractmethod
    def login(self, email: str, password: str):
        pass