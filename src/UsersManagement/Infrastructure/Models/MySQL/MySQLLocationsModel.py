from sqlalchemy import Column, Integer, Float, String, create_engine, ForeignKey
from src.Database.MySQL.connection import Base

class MySQLLocationsModel(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    uuid = Column(String, unique=True)
    latitude = Column(Float)
    altitude = Column(Float)
    longitude = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))

    def to_json(self):
        return {
            'id':self.id,
            'uuid':self.uuid,
            'latitude':self.latitude,
            'altitude':self.altitude,
            'longitude':self.longitude,
            'user_id':self.user_id
        }
