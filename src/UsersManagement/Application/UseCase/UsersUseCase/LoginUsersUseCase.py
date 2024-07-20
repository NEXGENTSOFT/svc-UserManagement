from src.UsersManagement.Domain.Ports.UsersPort import UsersPort as Port

class LoginUsersUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run(self, request):
        email: str = request['email']
        password: str = request['password']
        return self.port.login(email, password)
