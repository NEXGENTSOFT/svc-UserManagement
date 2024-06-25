import uuid

class Suscriptions:
    def __init__(self, starts_at, ends_at, user_id):
        self.uuid = uuid.uuid4()
        self.starts_at = starts_at
        self.ends_at = ends_at
        self.user_id = user_id
