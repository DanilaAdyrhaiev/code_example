from services import UserService
from models import Base
from database import engine
from flask import request

class UserController:
    def __init__(self, app):
        self.service = UserService()
        app.add_url_rule('/user', view_func=self.get_user, methods=['GET'])
        app.add_url_rule('/user/add', view_func=self.post_user, methods=['POST'])

    def get_user(self):
        id = int(request.args.get('id'))
        return self.service.get_user_by_id(id).to_dict()

    def post_user(self):
        data = request.get_json()
        name = data.get('username')
        email = data.get('email')
        return self.service.add_user(name, email).to_dict()