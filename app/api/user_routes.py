# app/api/user_routes.py
from fastapi import APIRouter
from app.services.user_service import get_user_details
from app.models.user_models import UserResponse

router = APIRouter()

@router.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def api_get_user(user_id: int):
    """
    API برای دریافت اطلاعات کاربر از طریق لایه Service
    """
    return get_user_details(user_id)
