from services.user_service.service import UserService
from services.user_service.schemas.user_schema import UserSchema

class UserController:
    def __init__(self):
        self.service = UserService()
        self.schema = UserSchema()

    def fetch_user(self, username):
        user = self.service.get_user(username)
        return self.schema.dump(user)
