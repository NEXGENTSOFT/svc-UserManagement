from src.UsersManagement.Domain.Ports.UsersPort import UsersPort as Port
from src.UsersManagement.Application.UseCase.UsersUseCase.CreateUsersUseCase import CreateUsersUseCase as UseCase


class CreateUsersController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, request):
        return self.use_case.run(request.get_json())
