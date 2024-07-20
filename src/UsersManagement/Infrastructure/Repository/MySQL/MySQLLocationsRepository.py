
from src.UsersManagement.Domain.Entity.Locations import Locations
from src.UsersManagement.Domain.Ports.LocationsPort import LocationsPort
from src.UsersManagement.Infrastructure.Models.MySQL.MySQLLocationsModel import MySQLLocationsModel
from src.Database.MySQL.connection import Base,engine,session_local

class MySQLLocationsRepository(LocationsPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_locations(self):
        pass

    def create_locations(self):
        pass

    def update_locations(self):
        pass


    def delete_locations(self):
        pass
