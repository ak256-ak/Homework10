from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    bio: Optional[str] = None  # Allow bio to be None
    profile_picture: Optional[str] = None  # Allow profile_picture to be None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
