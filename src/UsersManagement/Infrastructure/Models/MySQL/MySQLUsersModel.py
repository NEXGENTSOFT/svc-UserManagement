from sqlalchemy import Column, Integer, String,Date
from src.Database.MySQL.connection import Base


class MySQLUsersModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(36), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(36), nullable=False)
    username = Column(String(100), nullable=False)
    birthdate = Column(Date, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'name': self.name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'username': self.username,
            'birthdate': self.birthdate
        }