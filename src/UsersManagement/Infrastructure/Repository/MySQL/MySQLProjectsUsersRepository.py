from src.UsersManagement.Domain.Ports.ProjectsUsersPort import ProjectsUsersPort
from src.UsersManagement.Domain.Entity.ProjectsUsers import ProjectsUsers
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotCreatedError import NotCreatedError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotDeletedError import NotDeletedError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotFoundError import NotFoundError
from src.UsersManagement.Infrastructure.DTOS.Responses.BaseResponse import BaseResponse
from src.UsersManagement.Infrastructure.Models.MySQL.MySQLProjectsUsersModel import MySQLProjectsUsersModel as Model
from src.Database.MySQL.connection import Base, engine, session_local
from uuid import uuid4


class MySQLProjectsUsersRepository(ProjectsUsersPort):

    def __init__(self):
        Base.metadata.create_all(bind=engine)

    def get_projects_users(self, user_id):
        db = session_local()
        try:

            models = db.query(Model).filter(Model.user_id == user_id).all()
            if models is None:
                print(NotFoundError)
                raise NotFoundError
            print(f"Models found: {[str(m.project_id) for m in models]}")
            return {"data": [m.project_id for m in models], "session_uuid": str(uuid4())}
        except Exception as e:
            raise NotFoundError()

    def find_projects_users_by_uuid(self, uuid):
        db = session_local()
        try:
            model = db.query(Model).filter(Model.uuid == uuid).first()
            if model is None:
                raise NotFoundError
            return BaseResponse(
                success=True,
                message='Successfully fetched projects users',
                data=model.to_json()
            ).to_response()
        except Exception as e:
            raise NotFoundError()

    def create_projects_users(self, projects_users: ProjectsUsers):
        db = session_local()
        try:
            model = Model(uuid=projects_users.uuid, user_id=projects_users.user_id, project_id=projects_users.project_id)
            db.add(model)
            db.commit()
            response = BaseResponse(
                success=True,
                message='Successfully created projects users',
                data=model.to_json()
            )
            return response.to_response()
        except Exception as e:
            raise NotCreatedError()

    def delete_projects_users(self, relation_uuid):
        db = session_local()
        try:
            model = db.query(Model).filter(Model.uuid == relation_uuid).first()
            if model is None:
                raise NotFoundError
            db.delete(model)
            db.commit()
            response = BaseResponse(
                success=True,
                message='Successfully deleted projects users',
            ).to_response()
            return response
        except Exception as e:
            raise NotDeletedError()