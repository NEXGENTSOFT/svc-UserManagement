import uuid

class ProjectsUsers:
    def __init__(self, user_uuid, project_uuid):
        self.uuid = uuid.uuid4()
        self.user_uuid = user_uuid
        self.project_uuid = project_uuid