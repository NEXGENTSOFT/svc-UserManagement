import uuid

class ProjectsUsers:
    def __init__(self, user_id, project_id):
        self.uuid = uuid.uuid4()
        self.user_id = user_id
        self.project_id = project_id
