from repositories import UserRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User
from database import SessionLocal

class UserService:
    def __init__(self):
        self.repository = UserRepository(SessionLocal())

    def add_user(self, username: str, email: str) -> User | None:
        if username.strip() and email.strip():
            user = User(username=username, email=email)
            return self.repository.create(user)
        return None
    
    def get_user_by_id(self, id):
        if id:
            return self.repository.get_by_id(id)
        return None
        

