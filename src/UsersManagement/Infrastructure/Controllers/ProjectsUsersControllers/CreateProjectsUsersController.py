from src.UsersManagement.Domain.Ports.ProjectsUsersPort import ProjectsUsersPort as Port
from src.UsersManagement.Application.UseCase.ProjectsUsersUseCase.CreateProjectsUsersUseCase import CreateProjectsUsersUseCase as UseCase


class CreateProjectsUsersController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, request):
        return self.use_case.run(request)
