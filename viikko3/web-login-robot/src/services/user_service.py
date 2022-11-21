from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        if password != password_confirmation:
            raise UserInputError("Unmatching passwords")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        
        if re.match("[a-z]{3,}", username) and self._user_repository.find_by_username(username) is None:
            pass
        else:
            raise UserInputError("Username invalid or already in use")

        if re.match("\w*[^A-Za-z]+\w*", password) and len(password) >= 8:
            pass
        else:
            raise UserInputError("Password too short or contains only letters")


user_service = UserService()
