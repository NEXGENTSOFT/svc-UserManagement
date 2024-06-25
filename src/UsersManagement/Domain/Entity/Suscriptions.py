import uuid

class Suscriptions:
    def __init__(self, starts_at, ends_at, use_uuid):
        self.uuid = uuid.uuid4()
        self.starts_at = starts_at
        self.ends_at = ends_at
        self.use_uuid = use_uuid
