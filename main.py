from services import UserService
from models import Base
from database import engine

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    service = UserService()
    user = service.add_user("admin", "admin@example.com")
    print(user)
