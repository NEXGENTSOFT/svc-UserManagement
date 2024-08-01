from src.UsersManagement.Domain.Ports.ProjectsUsersPort import ProjectsUsersPort as Port
from src.UsersManagement.Application.UseCase.ProjectsUsersUseCase.DeleteProjectsUsersUseCase import DeleteProjectsUsersUseCase as UseCase


class DeleteProjectsUsersController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, user_id, project_id):
        return self.use_case.run(user_id, project_id)
