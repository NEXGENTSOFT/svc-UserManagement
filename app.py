from flask import Flask, jsonify, request

from src.UsersManagement.Infrastructure.Advices.Exceptions.NotFoundError import NotFoundError
from src.UsersManagement.Infrastructure.Advices.error_handlers import BaseError, handle_base_error
from src.UsersManagement.Infrastructure.Routes.UsersRoute import user_route
from src.UsersManagement.Infrastructure.Routes.SuscriptionsRoute import suscriptions_routes
from src.UsersManagement.Infrastructure.Routes.ProjectsUsersRoute import users_project_routes

app = Flask(__name__)

app.register_error_handler(BaseError, handle_base_error)
app.register_blueprint(user_route, url_prefix='/users')
app.register_blueprint(suscriptions_routes, url_prefix='/suscriptions')
app.register_blueprint(users_project_routes, url_prefix='/projects/users')

if __name__ == '__main__':
    app.run(port=5001)
