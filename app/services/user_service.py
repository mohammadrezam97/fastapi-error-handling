# app/services/user_service.py
from fastapi import HTTPException
from app.repositories.user_repository import get_user_by_id
from app.core.logger import logger
from app.models.user_models import UserResponse

def get_user_details(user_id: int) -> UserResponse:
    logger.info(f"Service: fetching details for user ID {user_id}")
    user = get_user_by_id(user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    logger.debug(f"Service: user found: {user}")
    return UserResponse(**user)
