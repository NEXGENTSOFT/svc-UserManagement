from src.UsersManagement.Domain.Entity.Locations import Locations
from src.UsersManagement.Domain.Ports.LocationsPort import LocationsPort as Port

class CreateLocationsUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        pass
