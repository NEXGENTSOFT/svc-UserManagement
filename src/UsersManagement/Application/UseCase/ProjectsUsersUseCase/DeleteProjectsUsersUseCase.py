from src.UsersManagement.Domain.Ports.ProjectsUsersPort import ProjectsUsersPort as Port


class DeleteProjectsUsersUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run(self, relation_uuid: str):
        return self.port.delete_projects_users(relation_uuid)
