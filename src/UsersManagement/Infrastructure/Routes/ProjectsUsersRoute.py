from flask import Blueprint, request

from src.UsersManagement.Infrastructure.Controllers.ProjectsUsersControllers.GetProjectsUsersController import GetProjectsUsersController as GetController
from src.UsersManagement.Infrastructure.Controllers.ProjectsUsersControllers.FindPorjectsUsersByUuidController import FindProjectsUsersByUuidController as FindController
from src.UsersManagement.Infrastructure.Controllers.ProjectsUsersControllers.CreateProjectsUsersController import CreateProjectsUsersController as CreateController
from src.UsersManagement.Infrastructure.Controllers.ProjectsUsersControllers.DeleteProjectsUsersController import DeleteProjectsUsersController as DeleteController

from src.UsersManagement.Infrastructure.Repository.MySQL.MySQLProjectsUsersRepository import MySQLProjectsUsersRepository as Repository

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

@users_project_routes.route("/", methods=['POST'])
def create_user_project():
    return create_controller.run(request)

@users_project_routes.route("/<string:uuid>", methods=['DELETE'])
def delete_user_project(uuid):
    return delete_controller.run(uuid)
