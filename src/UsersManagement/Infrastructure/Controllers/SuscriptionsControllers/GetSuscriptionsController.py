from src.UsersManagement.Domain.Ports.SuscriptionsPort import SuscriptionsPort as Port
from src.UsersManagement.Application.UseCase.SuscriptionsUseCase.GetSuscriptionsUseCase import GetSuscriptionsUseCase as UseCase


class GetSuscriptionsController:
    def __init__(self, port: Port):
        self.use_case = UseCase(port)

    def run(self, user_id):
        return self.use_case.run(user_id)
