from fastapi import APIRouter

router = APIRouter()

@router.get("/auth")
def auth_root():
    return {"message": "Auth routes are working!"}
