from src.UsersManagement.Domain.Ports.SuscriptionsPort import SuscriptionsPort as Port


class UpdateSuscriptionsUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run(self, request):
        start_date = request['start_date']
        uuid = request['uuid']
        return self.port.update_suscriptions(start_date, uuid)
