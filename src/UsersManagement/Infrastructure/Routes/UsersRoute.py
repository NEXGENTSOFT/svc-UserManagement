from flask import Blueprint, request
from src.UsersManagement.Infrastructure.Controllers.UsersControllers.GetUsersController import GetUsersController as GetController
from src.UsersManagement.Infrastructure.Controllers.UsersControllers.LoginUsersController import LoginUsersController as LoginController
from src.UsersManagement.Infrastructure.Controllers.UsersControllers.CreateUsersController import CreateUsersController as CreateController
from src.UsersManagement.Infrastructure.Controllers.UsersControllers.UpdateUsersController import UpdateUsersController as UpdateController
from src.UsersManagement.Infrastructure.Controllers.UsersControllers.DeleteUsersController import DeleteUsersController as DeleteController
from src.UsersManagement.Infrastructure.Repository.MySQL.MySQLUsersRepository import MySQLUsersRepository as Repository

repository = Repository()

get_controller = GetController(repository)
login_controller = LoginController(repository)
create_controller = CreateController(repository)
update_controller = UpdateController(repository)
delete_controller = DeleteController(repository)

user_route = Blueprint('UsersRoute', __name__)


@user_route.route("/<string:uuid>", methods=['GET'])
def get(uuid):
    return get_controller.run(uuid)

@user_route.route("/login", methods=['POST'])
def login():
    return login_controller.run(request)

@user_route.route("/", methods=['POST'])
def create():
    return create_controller.run(request)

@user_route.route("/", methods=['PUT'])
def update():
    return update_controller.run(request)

@user_route.route("/", methods=['DELETE'])
def delete():
    return delete_controller.run(request)
