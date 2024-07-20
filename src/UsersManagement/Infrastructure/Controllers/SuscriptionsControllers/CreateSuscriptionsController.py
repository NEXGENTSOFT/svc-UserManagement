from src.UsersManagement.Domain.Ports.SuscriptionsPort import SuscriptionsPort as Port
from src.UsersManagement.Application.UseCase.SuscriptionsUseCase.CreateSuscriptionsUseCase import CreateSuscriptionsUseCase as UseCase


class CreateSuscriptionsController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, request):
        return self.use_case.run(request.get_json())
