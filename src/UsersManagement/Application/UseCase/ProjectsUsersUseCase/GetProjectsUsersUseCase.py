from src.UsersManagement.Domain.Ports.ProjectsUsersPort import ProjectsUsersPort as Port
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotFoundError import NotFoundError
from src.UsersManagement.Infrastructure.Services.RabbitMQServices.ListProjectsUsersSagaProducer import ListProjectsUsersSagaProducer


class GetProjectsUsersUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run(self, user_id:int):
        new_request = self.port.get_projects_users(user_id)
        if new_request['data'] != []:
            saga_producer = ListProjectsUsersSagaProducer()
            return saga_producer.run(new_request)
        else:
            raise NotFoundError()
