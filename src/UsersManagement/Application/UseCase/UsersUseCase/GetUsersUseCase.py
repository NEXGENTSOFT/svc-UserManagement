from src.UsersManagement.Domain.Ports.UsersPort import UsersPort as Port

class GetUsersUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run(self, uuid):
        return self.port.get_users(uuid)
