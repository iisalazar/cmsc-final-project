from db import db


class AuthService:
    def login(self, username, password):
        # as of now, we hardcode the username and password
        # in the future, we will query the database to check if the username and password are correct
        return username == "test" and password == "test"
