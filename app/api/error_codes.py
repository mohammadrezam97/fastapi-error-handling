# app/api/error_codes.py
from fastapi import APIRouter
from app.core.error_codes import get_all_error_codes

router = APIRouter()

@router.get("/error-codes", tags=["System"])
def list_error_codes():
    """
    نمایش تمام کدهای خطا برای استفاده تیم توسعه یا DevOps
    """
    return get_all_error_codes()
