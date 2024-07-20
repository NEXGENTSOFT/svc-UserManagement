from src.UsersManagement.Domain.Ports.SuscriptionsPort import SuscriptionsPort as Port


class GetSuscriptionsUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run(self, user_id):
        self.port.get_suscriptions(user_id)
