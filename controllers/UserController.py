from services import UserService
from models import Base
from database import engine
from flask import request, jsonify
from flask import render_template
from DTOs import UserDTO


class UserController:
    def __init__(self, app):
        self.service = UserService()
        app.add_url_rule('/', view_func=self.index, methods=['GET'])
        app.add_url_rule('/submit', view_func=self.submit, methods=['POST'])
        app.add_url_rule('/user', view_func=self.get_user, methods=['GET'])
        # app.add_url_rule('/user/add', view_func=self.post_user, methods=['POST'])

    def get_user(self):
        id = int(request.args.get('id'))
        return self.service.get_user_by_id(id).to_dict()

    def index(self):
        return render_template('index.html')
    
    def submit(self):
        name = request.form['fname']
        email = request.form['femail']
        added_user = self.service.add_user(UserDTO(username= name, email= email))
        return jsonify(added_user.model_dump())


    # def post_user(self):
    #     data = request.get_json()
    #     if data.get('username').strip() and data.get('email').strip():
    #         user_dto = UserDTO(username= data.get('username'), email=data.get('email'))
    #         added_user = self.service.add_user(user_dto)
    #         return jsonify(added_user.model_dump())