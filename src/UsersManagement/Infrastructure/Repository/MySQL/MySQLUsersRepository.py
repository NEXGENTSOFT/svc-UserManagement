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
from datetime import datetime


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
            hashed = hash_password(user.password)
            newUser = Model(
                uuid=user.uuid,
                name=user.name,
                last_name=user.last_name,
                email=user.email,
                password=hashed,
                username=user.username,
                birthdate=datetime.strptime(user.birthdate, '%Y-%m-%d').date()
            )
            self.db.add(newUser)
            self.db.commit()
            token = write_token(data={"username": newUser.username, "user_uuid": newUser.uuid})
            response = BaseResponse(
                success=True,
                message='Successfully created new user',
                data={"user": newUser.to_json(), "token": token}
            )
            return response.to_response()
        except Exception as e:
            raise NotCreatedError()

    def update_users(self, uuid: str, newPassword: str, password: str, username: str):
        try:
            model = self.db.query(Model).filter(Model.uuid == uuid).first()
            if model is None:
                raise NotFoundError()

            if newPassword is not None:
                if check_password(password, model.password):
                    model.password = hash_password(newPassword)
                    print("New hashed password:", model.password)
                    print("Committing new password...")
                    self.db.commit()
                    print("Password committed successfully")
                else:
                    raise LoginFailedError()

            if username is not None:
                model.username = username
                print("Committing new username...")
                self.db.commit()
                print("Username committed successfully")

            response = BaseResponse(
                success=True,
                message='Successfully updated user',
                data=model.to_json()
            )
            return response.to_response()
        except Exception as e:
            print(f"Error updating user: {e}")
            self.db.rollback()
            raise NotUpdatedError()

    def delete_users(self, uuid: str, password: str):
        try:
            model = self.db.query(Model).filter(Model.uuid == uuid).first()
            self.db.delete(model)
            self.db.commit()
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
                token = write_token(data={"username": model.username, "user_uuid": model.uuid})
                response = BaseResponse(
                    success=True,
                    message='Successfully logged in',
                    data={"user": model.to_json(), "token": token}
                )
                return response.to_response()
            else:
                raise LoginFailedError()
        except Exception as e:
            raise LoginFailedError()