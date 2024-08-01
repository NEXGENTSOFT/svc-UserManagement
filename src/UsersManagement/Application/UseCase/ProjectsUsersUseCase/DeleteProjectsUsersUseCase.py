from src.UsersManagement.Domain.Ports.ProjectsUsersPort import ProjectsUsersPort as Port


class DeleteProjectsUsersUseCase:
    def __init__(self, port: Port):
        self.port = port

    def run(self, user_id, project_id):
        return self.port.delete_projects_users(user_id, project_id)
