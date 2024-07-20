from src.UsersManagement.Domain.Ports.ProjectsUsersPort import ProjectsUsersPort as Port
from src.UsersManagement.Application.UseCase.ProjectsUsersUseCase.FindProjectsUserByUuidUseCase import FindProjectsUserByUuidUseCase as UseCase


class FindProjectsUsersByUuidController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, uuid):
        return self.use_case.run(uuid)
