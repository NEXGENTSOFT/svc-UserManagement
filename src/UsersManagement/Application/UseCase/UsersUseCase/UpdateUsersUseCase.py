from src.UsersManagement.Domain.Ports.UsersPort import UsersPort as Port

class UpdateUsersUseCase:
    def __init__(self, port:Port):
        self.port = port

    def run(self, request):
        uuid = request['uuid']
        userName = request['userName']
        password = request['password']
        newPassword = request['newPassword']
        return self.port.update_users(uuid, newPassword, password, userName)
