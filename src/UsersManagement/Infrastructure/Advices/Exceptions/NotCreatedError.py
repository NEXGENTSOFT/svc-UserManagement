from src.UsersManagement.Infrastructure.Advices.BaseError import BaseError


class NotCreatedError(BaseError):
    def __init__(self, message="Resource could not be created", data=None):
        super().__init__(message, status_code=400, data=data)