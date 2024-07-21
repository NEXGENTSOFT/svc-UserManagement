from src.UsersManagement.Domain.Entity.Users import Users
from src.UsersManagement.Infrastructure.Advices.Exceptions.LoginFailedError import LoginFailedError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotCreatedError import NotCreatedError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotDeletedError import NotDeletedError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotFoundError import NotFoundError
from src.UsersManagement.Infrastructure.Advices.Exceptions.NotUpdatedError import NotUpdatedError
from src.UsersManagement.Infrastructure.DTOS.Responses.BaseResponse import BaseResponse
from src.UsersManagement.Infrastructure.Models.MySQL.MySQLUsersModel import MySQLUsersModel as Model
from src.UsersManagement.Domain.Ports.UsersPort import UsersPort
from src.Database.MySQL.connection import Base, engine, session_local
from src.UsersManagement.Infrastructure.Utilities.password_utils import hash_password, check_password
from src.UsersManagement.Infrastructure.Middlewares.functionsJWT import write_token

class MySQLUsersRepository(UsersPort):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_users(self, uuid: str):
        try:
            user = self.db.query(Model).filter(Model.uuid == uuid).first()
            if user is None:
                raise NotFoundError()
            response = BaseResponse(
                success=True,
                message='Successfully fetched user data',
                data=user.to_json()
            )
            return response.to_response()
        except Exception as e:
            raise NotFoundError()

    def create_users(self, user: Users):
        try:
            newUser = Model(**user.__dict__)
            self.db.add(newUser)
            self.db.commit()
            token = write_token(user.to_json())
            response = BaseResponse(
                success=True,
                message='Successfully created new user',
                data={"user": newUser.to_json(), "token": token}
            )
            return response.to_response()
        except Exception as e:
            raise NotCreatedError()
    def update_users(self, uuid: str, password: str, username: str):
        try:
            model = self.db.query(Model).filter(Model.uuid == uuid).first()
            if model is None:
                raise NotFoundError()
            if password is not None:
                if check_password(password, model.password):
                    model.password = hash_password(password)
                else:
                    raise LoginFailedError()
            model.username = username
            self.db.commit()
            response = BaseResponse(
                success=True,
                message='Successfully updated user',
                data=model.to_json()
            )
            return response.to_response()
        except Exception as e:
            raise NotUpdatedError()

    def delete_users(self, uuid: str, password: str):
        try:
            model = self.db.query(Model).filter(Model.uuid == uuid).first()
            if model is None:
                raise NotFoundError()
            response = BaseResponse(
                success=True,
                message='Successfully deleted user',
                data=model.to_json()
            )
            return response.to_response()
        except Exception as e:
            raise NotDeletedError()

    def login(self, email: str, password: str):
        try:
            model = self.db.query(Model).filter(Model.email == email).first()
            if model is None:
                raise NotFoundError()
            if check_password(password, model.password):
                token = write_token(model.to_json())
                response = BaseResponse(
                    success=True,
                    message='Successfully logged in',
                    data={"user": model.to_json(), token: token}
                )
                return response.to_response()
            else:
                raise LoginFailedError()
        except Exception as e:
            raise LoginFailedError()