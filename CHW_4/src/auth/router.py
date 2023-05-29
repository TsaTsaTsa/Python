from fastapi import APIRouter, Depends

from src.auth.base_config import fastapi_users, auth_backend
from src.auth.schemas import UserRead, UserCreate
from src.auth.base_config import current_user


router_reg = fastapi_users.get_register_router(UserRead, UserCreate)
router_auth = fastapi_users.get_auth_router(auth_backend)

router_info = APIRouter(prefix="/auth", tags=["Auth"])


@router_info.get("/get_info")
def get_info_about_user(user: UserRead = Depends(current_user)):
    return {'user_id': user.id, 'username': user.username, 'email': user.email, 'role': user.role_name}
