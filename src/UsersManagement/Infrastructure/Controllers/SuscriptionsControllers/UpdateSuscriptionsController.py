from src.UsersManagement.Domain.Ports.SuscriptionsPort import SuscriptionsPort as Port
from src.UsersManagement.Application.UseCase.SuscriptionsUseCase.UpdateSuscriptionsUseCase import UpdateSuscriptionsUseCase as UseCase


class UpdateSuscriptionsController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, request):
        return self.use_case.run(request)
