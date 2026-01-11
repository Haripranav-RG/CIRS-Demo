from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserRegisterRequest
from app.models.user import User
from app.core.security import hash_password

class UserService:

    def __init__(self):
        self.user_repo = UserRepository()

    def register_user(
        self,
        db: Session,
        data: UserRegisterRequest
    ) -> User:

        if self.user_repo.get_by_email(db, data.email):
            raise ValueError("Email already registered")

        user = User(
            full_name=data.full_name,
            email=data.email,
            phone=data.phone,
            password_hash=hash_password(data.password),
            role="USER"
        )

        return self.user_repo.create(db, user)
