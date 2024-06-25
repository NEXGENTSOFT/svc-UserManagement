import uuid


class Users:
    def __init__(self, name, lastname, email, password, username, birthday):
        self.uuid = uuid.uuid4()
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.username = username
        self.birthday = birthday
