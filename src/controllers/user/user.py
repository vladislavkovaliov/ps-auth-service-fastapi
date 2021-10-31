from src.models.user import User


class UserController:
    def get(self) -> User:
        user = User(name="123")
        return user