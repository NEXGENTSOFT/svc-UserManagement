from src.UsersManagement.Domain.Ports.ProjectsUsersPort import ProjectsUsersPort as Port


class FindProjectsUserByUuidUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run(self, uuid:str):
        return self.port.find_projects_users_by_uuid(uuid)
