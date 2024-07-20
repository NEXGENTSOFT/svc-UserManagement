from src.UsersManagement.Domain.Ports.UsersPort import UsersPort as Port

class DeleteUsersUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run(self, request):
        uuid = request['uuid']
        password = request['password']
        return self.port.delete_users(uuid, password)
