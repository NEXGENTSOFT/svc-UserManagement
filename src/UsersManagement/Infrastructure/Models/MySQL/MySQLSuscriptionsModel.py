from sqlalchemy import Column, Integer, Float, String, create_engine, ForeignKey, Date
from src.Database.MySQL.connection import Base

class MySQLSuscriptionsModel(Base):
    __tablename__ = 'suscriptions'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), unique=True, nullable=False)
    starts = Column(Date, nullable=False)
    ends_at = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'starts': self.starts,
            'ends_at': self.ends_at,
            'user_id': self.user_id
        }