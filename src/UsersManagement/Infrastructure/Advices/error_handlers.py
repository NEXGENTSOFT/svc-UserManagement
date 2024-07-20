from flask import jsonify
from src.UsersManagement.Infrastructure.Advices.BaseError import BaseError

def handle_base_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response