from src.UsersManagement.Domain.Entity.Users import Users
from src.UsersManagement.Domain.Ports.UsersPort import UsersPort as Port

class CreateUsersUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run (self, request):
        users = Users(**request)
        return self.port.create_users(users)
