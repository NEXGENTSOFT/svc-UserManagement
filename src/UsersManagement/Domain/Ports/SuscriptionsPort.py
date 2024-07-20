from abc import ABC, abstractmethod
from src.UsersManagement.Domain.Entity.Suscriptions import Suscriptions
class SuscriptionsPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_suscriptions(self, user_id):
        pass

    @abstractmethod
    def create_suscriptions(self, suscriptions: Suscriptions):
        pass

    @abstractmethod
    def update_suscriptions(self, new_start_date, uuid):
        pass

    @abstractmethod
    def delete_suscriptions(self, suscription_uuid):
        pass