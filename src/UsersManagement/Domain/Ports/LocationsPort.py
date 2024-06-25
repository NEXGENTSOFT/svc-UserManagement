from abc import ABC, abstractmethod
from src.UsersManagement.Domain.Entity.Locations import Locations

class LocationsPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_locations(self):
        pass

    @abstractmethod
    def create_locations(self):
        pass

    @abstractmethod
    def update_locations(self):
        pass

    @abstractmethod
    def delete_locations(self):
        pass
