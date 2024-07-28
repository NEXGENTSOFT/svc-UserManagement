from flask import Flask, jsonify, request
from flask_cors import CORS
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotFoundError import NotFoundError
from src.UsersManagement.Infrastructure.Advices.error_handlers import BaseError, handle_base_error
from src.UsersManagement.Infrastructure.Routes.UsersRoute import user_route
from src.UsersManagement.Infrastructure.Routes.SuscriptionsRoute import suscriptions_routes
from src.UsersManagement.Infrastructure.Routes.ProjectsUsersRoute import users_project_routes, create_user_project_thread

app = Flask(__name__)

# Configuración de error handlers
app.register_error_handler(BaseError, handle_base_error)

# Registro de rutas
app.register_blueprint(user_route, url_prefix='/users')
app.register_blueprint(suscriptions_routes, url_prefix='/suscriptions')
app.register_blueprint(users_project_routes, url_prefix='/projects/users')
CORS(app)

def start_services(app):
    create_user_project_thread(app)


if __name__ == '__main__':
    start_services(app)
    app.run(debug=True, port=5001)


