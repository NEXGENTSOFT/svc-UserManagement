from abc import ABC, abstractmethod
from src.UsersManagement.Domain.Entity.ProjectsUsers import ProjectsUsers
class ProjectsUsersPort(ABC):
        @abstractmethod
        def __init__(self):
            pass

        @abstractmethod
        def get_projects_users(self, user_id):
            pass

        @abstractmethod
        def find_projects_users_by_uuid(self, uuid):
            pass

        @abstractmethod
        def create_projects_users(self, projects_users: ProjectsUsers):
            pass

        @abstractmethod
        def delete_projects_users(self, relation_uuid: str):
            pass