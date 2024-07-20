class BaseError(Exception):
    def __init__(self, message, status_code=400, data=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.data = data

    def to_dict(self):
        error_response = {
            'error': self.message,
            'status_code': self.status_code,
        }
        if self.data:
            error_response['data'] = self.data
        return error_response
