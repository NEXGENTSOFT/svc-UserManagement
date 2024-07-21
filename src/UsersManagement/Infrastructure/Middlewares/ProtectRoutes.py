from flask import jsonify, request
from src.UsersManagement.Infrastructure.Middlewares.functionsJWT import validate_token


def token_required(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"Message": "A valid token is missing", "status": "error"}), 403
        try:
            validate_token(token)
        except Exception as e:
            return jsonify({"Message": str(e), "status": "error"}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper