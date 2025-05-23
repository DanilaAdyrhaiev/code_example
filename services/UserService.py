from repositories import UserRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User
from DTOs import UserDTO
from mappers import UserMapper
from database import SessionLocal


class UserService:
    def __init__(self):
        self.repository = UserRepository(SessionLocal())

    def add_user(self, user_dto: UserDTO) -> User | None:
        created_user = self.repository.create(UserMapper.from_dto(user_dto))
        if created_user:
            return UserMapper.to_dto(created_user)
        return None
    
    def get_user_by_id(self, id):
        if id:
            return self.repository.get_by_id(id)
        return None
        

