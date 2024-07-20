from flask import Blueprint, request

from src.UsersManagement.Infrastructure.Controllers.SuscriptionsControllers.GetSuscriptionsController import GetSuscriptionsController as GetController
from src.UsersManagement.Infrastructure.Controllers.SuscriptionsControllers.CreateSuscriptionsController import \
    CreateSuscriptionsController as CreateController, CreateSuscriptionsController
from src.UsersManagement.Infrastructure.Controllers.SuscriptionsControllers.UpdateSuscriptionsController import UpdateSuscriptionsController as UpdateController
from src.UsersManagement.Infrastructure.Controllers.SuscriptionsControllers.DeleteSuscriptionsController import DeleteSuscriptionsController as DeleteController

from src.UsersManagement.Infrastructure.Repository.MySQL.MySQLSuscriptionsRepository import MySQLSuscriptionsRepository as Repository

repository = Repository()

get_controller = GetController(repository)
create_controller = CreateController(repository)
update_controller = UpdateController(repository)
delete_controller = DeleteController(repository)

suscriptions_routes = Blueprint('SuscriptionsRoutes', __name__)

@suscriptions_routes.route("/<int:id>", methods=['GET'])
def get_suscriptions(id):
    return get_controller.run(id)

@suscriptions_routes.route("/", methods=['POST'])
def create_suscriptions():
    return create_controller.run(request)

@suscriptions_routes.route("/", methods=['PUT'])
def update_suscriptions():
    return update_controller.run(request)

@suscriptions_routes.route("/<string: uuid>", methods=['DELETE'])
def delete_suscriptions(uuid):
    return delete_controller.run(uuid)
