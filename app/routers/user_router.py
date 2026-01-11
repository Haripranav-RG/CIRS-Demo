from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.services.user_service import UserService
from app.schemas.user_schema import (
    UserRegisterRequest,
    UserRegisterResponse
)

router = APIRouter(prefix="/users", tags=["Users"])


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Service Dependency
def get_user_service():
    return UserService()


@router.post(
    "/register",
    response_model=UserRegisterResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    request: UserRegisterRequest,
    db: Session = Depends(get_db),
    service: UserService = Depends(get_user_service)
):
    try:
        return service.register_user(db=db, data=request)

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong"
        )
