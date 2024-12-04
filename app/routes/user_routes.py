from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserOut
from app.services.user_service import create_user, get_user_by_username
from app.database import get_db

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return create_user(db, user)
