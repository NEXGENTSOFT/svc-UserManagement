from src.UsersManagement.Domain.Ports.SuscriptionsPort import SuscriptionsPort as Port
from src.UsersManagement.Application.UseCase.SuscriptionsUseCase.DeleteSuscriptionsUseCase import DeleteSuscriptionsUseCase as UseCase


class DeleteSuscriptionsController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, uuid):
        return self.use_case.run(uuid)
