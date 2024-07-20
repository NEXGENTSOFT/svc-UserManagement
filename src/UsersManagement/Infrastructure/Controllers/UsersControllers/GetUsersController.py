from src.UsersManagement.Domain.Ports.UsersPort import UsersPort as Port
from src.UsersManagement.Application.UseCase.UsersUseCase.GetUsersUseCase import GetUsersUseCase as UseCase


class GetUsersController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, uuid: str):
        return self.use_case.run(uuid)
