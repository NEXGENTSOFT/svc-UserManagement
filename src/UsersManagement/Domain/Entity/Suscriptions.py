import uuid

class Suscriptions:
    def __init__(self, user_id):
        self.uuid = uuid.uuid4()
        self.user_id = user_id
