from src.UsersManagement.Infrastructure.Advices.BaseError import BaseError


class InvalidTypeError(BaseError):
    def __init__(self, message="Invalid type", data=None):
        super().__init__(message, status_code=400, data=data)
