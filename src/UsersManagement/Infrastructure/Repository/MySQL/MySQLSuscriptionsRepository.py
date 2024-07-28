import uuid

from src.UsersManagement.Domain.Entity.Suscriptions import Suscriptions
from src.UsersManagement.Domain.Ports.SuscriptionsPort import SuscriptionsPort
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotCreatedError import NotCreatedError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotDeletedError import NotDeletedError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotFoundError import NotFoundError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotUpdatedError import NotUpdatedError
from src.UsersManagement.Infrastructure.DTOS.Responses.BaseResponse import BaseResponse
from src.UsersManagement.Infrastructure.Models.MySQL.MySQLSuscriptionsModel import MySQLSuscriptionsModel as Model
from src.Database.MySQL.connection import Base, engine, session_local
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class MySQLSuscriptionsRepository(SuscriptionsPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)

    def get_suscriptions(self, user_id):
        db = session_local()
        try:
            model = db.query(Model).filter(Model.user_id == user_id).first()
            if model is None:
                raise NotFoundError()
            return BaseResponse(
                success=True,
                message='Suscriptions found',
                data=model.to_json()
            ).to_response()
        except Exception as e:
            raise NotFoundError()

    def create_suscriptions(self, suscriptions: Suscriptions):
        db = session_local()
        try:
            model = Model(starts=datetime.now(), user_id=suscriptions.user_id, uuid=suscriptions.uuid, ends_at=datetime.now()+timedelta(days=7))
            db.add(model)
            db.commit()
            return BaseResponse(
                success=True,
                message='Suscriptions created',
                data=model.to_json(),
                status_code=201
            ).to_response()
        except Exception as e:
            raise NotCreatedError()

    def update_suscriptions(self, uuid):
        db = session_local()
        try:
            model = db.query(Model).filter(Model.uuid == uuid).first()
            if model is None:
                raise NotFoundError()
            model.start_date = datetime.now()
            model.ends_at = datetime.now() + relativedelta(months=1)
            db.commit()
            return BaseResponse(
                success=True,
                message='Suscriptions updated',
                data=model.to_json()
            ).to_response()
        except Exception as e:
            raise NotUpdatedError()

    def delete_suscriptions(self, suscription_uuid):
        db = session_local()
        try:
            model = db.query(Model).filter(Model.uuid == suscription_uuid).first()
            if model is None:
                raise NotFoundError()
            db.delete(model)
            db.commit()
            return BaseResponse(
                success=True,
                message='Suscriptions deleted'
            ).to_response()
        except Exception as e:
            raise NotDeletedError()
