from abc import ABC, abstractmethod
from src.UsersManagement.Domain.Entity.Locations import Locations

class LocationsPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_clima(self, location:Locations):
        pass