from sqlalchemy import Column, Integer, Float, String, create_engine, ForeignKey
from src.Database.MySQL.connection import Base


class MySQLProjectsUsersModel(Base):
    __tablename__ = 'projects_users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(36), unique=True, nullable=False)
    project_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'project_id': self.project_id,
            'user_id': self.user_id
        }
