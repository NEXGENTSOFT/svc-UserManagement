from src.UsersManagement.Infrastructure.Advices.BaseError import BaseError


class LoginFailedError(BaseError):
    def __init__(self, message="Login failed", data=None):
        super().__init__(message, status_code=401, data=data)
