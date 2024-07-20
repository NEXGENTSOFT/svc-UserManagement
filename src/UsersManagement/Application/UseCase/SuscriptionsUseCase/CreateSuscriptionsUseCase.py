from src.UsersManagement.Domain.Ports.SuscriptionsPort import SuscriptionsPort as Port
from src.UsersManagement.Domain.Entity.Suscriptions import Suscriptions as Entity


class CreateSuscriptionsUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run(self, request):
        entity = Entity(**request)
        return self.port.create_suscriptions(entity)
