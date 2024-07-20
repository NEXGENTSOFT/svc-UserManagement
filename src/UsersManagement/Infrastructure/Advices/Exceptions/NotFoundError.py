from src.UsersManagement.Infrastructure.Advices.BaseError import BaseError


class NotFoundError(BaseError):
    def __init__(self, message="Resource not found", data=None):
        super().__init__(message, status_code=404, data=data)
