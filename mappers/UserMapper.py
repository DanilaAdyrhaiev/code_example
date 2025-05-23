from models import User
from DTOs import UserDTO

class UserMapper:
    @classmethod
    def from_dto(cls, dto: UserDTO) -> User:
        user = User()
        user.username = dto.username
        user.email = dto.email
        return user
    
    @classmethod
    def to_dto(cls, user: User):
        user_dto = UserDTO(username=user.username, email=user.email)
        return user_dto