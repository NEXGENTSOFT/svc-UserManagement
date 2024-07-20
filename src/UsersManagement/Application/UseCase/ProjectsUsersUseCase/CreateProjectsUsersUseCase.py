from src.UsersManagement.Domain.Ports.ProjectsUsersPort import ProjectsUsersPort as Port
from src.UsersManagement.Domain.Entity.ProjectsUsers import ProjectsUsers as Entity


class CreateProjectsUsersUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run(self, request):
        entity = Entity(**request.__dict__)
        return self.port.create_projects_users(entity)
