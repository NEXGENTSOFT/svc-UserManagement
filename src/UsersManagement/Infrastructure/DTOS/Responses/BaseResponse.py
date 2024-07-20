from flask import jsonify

class BaseResponse:
    def __init__(self, success: bool, message: str, data=None, status_code=200):
        self.success = success
        self.message = message
        self.data = data
        self.status_code = status_code

    def to_dict(self):
        response = {
            'success': self.success,
            'message': self.message,
        }
        if self.data is not None:
            response['data'] = self.data
        return response

    def to_response(self):
        return jsonify(self.to_dict()), self.status_code
