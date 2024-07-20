from src.UsersManagement.Domain.Entity.Suscriptions import Suscriptions
from src.UsersManagement.Domain.Ports.SuscriptionsPort import SuscriptionsPort
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotCreatedError import NotCreatedError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotDeletedError import NotDeletedError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotFoundError import NotFoundError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotUpdatedError import NotUpdatedError
from src.UsersManagement.Infrastructure.DTOS.Responses.BaseResponse import BaseResponse
from src.UsersManagement.Infrastructure.Models.MySQL.MySQLSuscriptionsModel import MySQLSuscriptionsModel as Model
from src.Database.MySQL.connection import Base, engine, session_local


class MySQLSuscriptionsRepository(SuscriptionsPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_suscriptions(self, user_id):
        try:
            model = self.db.get(Model.user_id == user_id)
            if model is None:
                raise NotFoundError()
            return BaseResponse(
                success=True,
                message='Suscriptions found',
                data=model.to_json()
            )
        except Exception as e:
            raise NotFoundError()

    def create_suscriptions(self, suscriptions: Suscriptions):
        try:
            model = Model(**suscriptions.__dict__)
            self.db.add(model)
            self.db.commit()
            return BaseResponse(
                success=True,
                message='Suscriptions created',
                data=model.to_json(),
                status_code=201
            )
        except Exception as e:
            raise NotCreatedError()

    def update_suscriptions(self, new_start_date, uuid):
        try:
            model = self.db.query(Model).filter(Model.uuid == uuid).first()
            if model is None:
                raise NotFoundError()
            model.start_date = new_start_date
            self.db.commit()
            return BaseResponse(
                success=True,
                message='Suscriptions updated',
                data=model.to_json()
            )
        except Exception as e:
            raise NotUpdatedError()

    def delete_suscriptions(self, suscription_uuid):
        try:
            model = self.db.query(Model).filter(Model.uuid == suscription_uuid).first()
            if model is None:
                raise NotFoundError()
            self.db.delete(model)
            self.db.commit()
            return BaseResponse(
                success=True,
                message='Suscriptions deleted'
            )
        except Exception as e:
            raise NotDeletedError()
