from abc import ABC, abstractmethod
from src.UsersManagement.Domain.Entity.ProjectsUsers import ProjectsUsers
class ProjectsUsersPort(ABC):
        @abstractmethod
        def __init__(self):
            pass

        @abstractmethod
        def get_projects_users(self):
            pass

        @abstractmethod
        def create_projects_users(self):
            pass

        @abstractmethod
        def update_projects_users(self):
            pass

        @abstractmethod
        def delete_projects_users(self):
            pass