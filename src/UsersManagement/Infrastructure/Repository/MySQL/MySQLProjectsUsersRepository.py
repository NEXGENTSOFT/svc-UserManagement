from src.UsersManagement.Domain.Ports.ProjectsUsersPort import ProjectsUsersPort
from src.UsersManagement.Domain.Entity.ProjectsUsers import ProjectsUsers
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotCreatedError import NotCreatedError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotDeletedError import NotDeletedError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotFoundError import NotFoundError
from src.UsersManagement.Infrastructure.DTOS.Responses.BaseResponse import BaseResponse
from src.UsersManagement.Infrastructure.Models.MySQL.MySQLProjectsUsersModel import MySQLProjectsUsersModel as Model
from src.Database.MySQL.connection import Base, engine, session_local


class MySQLProjectsUsersRepository(ProjectsUsersPort):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_projects_users(self, user_id):
        try:
            models = self.db.query(Model).filter(Model.user_id == user_id).all()
            if models is None:
                raise NotFoundError
            response = BaseResponse(
                success=True,
                message='Successfully fetched projects users',
                data=[m.to_json() for m in models]
            )
            return response.to_response()
        except Exception as e:
            raise NotFoundError()

    def find_projects_users_by_uuid(self, uuid):
        try:
            model = self.db.query(Model).filter(Model.uuid == uuid).first()
            if model is None:
                raise NotFoundError
            return BaseResponse(
                success=True,
                message='Successfully fetched projects users',
                data=model.to_json()
            )
        except Exception as e:
            raise NotFoundError()

    def create_projects_users(self, projects_users: ProjectsUsers):
        try:
            model = Model(**projects_users.__dict__)
            self.db.add(model)
            self.db.commit()
            response = BaseResponse(
                success=True,
                message='Successfully created projects users',
                data=model.to_json()
            )
            return response.to_response()
        except Exception as e:
            raise NotCreatedError()

    def delete_projects_users(self, relation_uuid):
        try:
            model = self.db.query(Model).filter(Model.uuid == relation_uuid).first()
            if model is None:
                raise NotFoundError
            self.db.delete(model)
            self.db.commit()
            response = BaseResponse(
                success=True,
                message='Successfully deleted projects users',
            )
            return response.to_response()
        except Exception as e:
            raise NotDeletedError()