from src.UsersManagement.Domain.Ports.SuscriptionsPort import SuscriptionsPort as Port


class DeleteSuscriptionsUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run(self, uuid: str):
        return self.port.delete_suscriptions(uuid)
