from src.UsersManagement.Domain.Ports.ProjectsUsersPort import ProjectsUsersPort as Port
from src.UsersManagement.Application.UseCase.ProjectsUsersUseCase.GetProjectsUsersUseCase import GetProjectsUsersUseCase as UseCase


class GetProjectsUsersController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, user_id: int):
        return self.use_case.run(user_id)

