from flask import Blueprint, request
import threading
from src.UsersManagement.Infrastructure.Controllers.ProjectsUsersControllers.GetProjectsUsersController import GetProjectsUsersController as GetController
from src.UsersManagement.Infrastructure.Controllers.ProjectsUsersControllers.FindPorjectsUsersByUuidController import FindProjectsUsersByUuidController as FindController
from src.UsersManagement.Infrastructure.Controllers.ProjectsUsersControllers.CreateProjectsUsersController import \
    CreateProjectsUsersController as CreateController, CreateProjectsUsersController
from src.UsersManagement.Infrastructure.Controllers.ProjectsUsersControllers.DeleteProjectsUsersController import DeleteProjectsUsersController as DeleteController
from src.UsersManagement.Infrastructure.Repository.MySQL.MySQLProjectsUsersRepository import MySQLProjectsUsersRepository as Repository
from src.UsersManagement.Infrastructure.Services.RabbitMQServices.CreateProjectUserConsumer import \
    CreateProjectUserConsumer

repository = Repository()

get_controller = GetController(repository)
find_controller = FindController(repository)
create_controller = CreateController(repository)
delete_controller = DeleteController(repository)

users_project_routes = Blueprint('users_project_routes', __name__)

@users_project_routes.route("/<int:user_id>", methods=['GET'])
def get_project_users(user_id):
    return get_controller.run(user_id)

@users_project_routes.route("/find/<string:uuid>", methods=['GET'])
def find_project_user(uuid):
    return find_controller.run(uuid)

#@users_project_routes.route("/", methods=['POST'])
def create_user_project_thread(app):
    create_projects_users_consumer = CreateProjectUserConsumer(create_controller, app)
    thread = threading.Thread(target=create_projects_users_consumer.start_consuming_queue_create_project_user)
    thread.daemon = True
    thread.start()

@users_project_routes.route("/<string:uuid>", methods=['DELETE'])
def delete_user_project(uuid):
    return delete_controller.run(uuid)
