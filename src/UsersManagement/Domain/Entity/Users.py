import uuid
import re
from datetime import datetime
from src.UsersManagement.Infrastructure.Utilities.password_utils import hash_password


class ValidationError(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {'error': self.message}


class Users:
    def __init__(self, name: str, last_name: str, email: str, password: str, username: str, birthdate: str):
        self.uuid = uuid.uuid4()
        self.name = self._validate_name(name)
        self.last_name = self._validate_lastname(last_name)
        self.email = self._validate_email(email)
        self.password = self._validate_password(password)
        self.username = self._validate_username(username)
        self.birthdate = self._validate_birthday(birthdate)

    def _validate_name(self, name):
        if isinstance(name, str) and name.isalpha():
            return name
        else:
            raise ValidationError("Invalid name")

    def _validate_lastname(self, lastname):
        if isinstance(lastname, str) and lastname.isalpha():
            return lastname
        else:
            raise ValidationError("Invalid lastname")

    def _validate_email(self, email):
        if not isinstance(email, str):
            raise ValidationError("Email must be a string")
        regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(regex, email):
            return email
        else:
            raise ValidationError("Invalid email")

    def _validate_password(self, password):
        if not isinstance(password, str):
            raise ValidationError("Password must be a string")
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must contain at least one uppercase letter")
        if not re.search(r'[a-z]', password):
            raise ValidationError("Password must contain at least one lowercase letter")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>\-+]', password):
            raise ValidationError("Password must contain at least one special character")
        return password

    def _validate_username(self, username):
        if isinstance(username, str) and len(username) >= 3:
            return username
        else:
            raise ValidationError("Invalid username")

    def _validate_birthday(self, birthday):
        if not isinstance(birthday, str):
            raise ValidationError("Birthday must be a string")
        try:
            datetime.strptime(birthday, '%Y-%m-%d')
            return birthday
        except ValueError:
            raise ValidationError("Invalid birthday format, should be YYYY-MM-DD")
