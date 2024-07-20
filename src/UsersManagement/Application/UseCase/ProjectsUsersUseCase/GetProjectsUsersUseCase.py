from src.UsersManagement.Domain.Ports.ProjectsUsersPort import ProjectsUsersPort as Port


class GetProjectsUsersUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run(self, user_id:int):
        return self.port.get_projects_users(user_id)
