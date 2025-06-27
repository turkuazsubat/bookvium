from fastapi import APIRouter, Depends
from app.schemas.user import UserOut
from app.utils.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
