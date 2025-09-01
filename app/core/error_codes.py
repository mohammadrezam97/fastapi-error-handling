# app/core/error_codes.py
from datetime import datetime

# ساختار کد: SERVICE-SUBSERVICE-XXX
ERROR_CODES = {
    "USR-AUTH-001": "User authentication failed",
    "USR-AUTH-002": "User not found",
    "USR-REG-001": "User already exists",
    "FLG-FND-001": "Flight not found",
    "FLG-RSV-001": "Seat is unavailable",
}

def get_all_error_codes():
    """برگشت تمام کدهای خطا با timestamp"""
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "count": len(ERROR_CODES),
        "errors": ERROR_CODES
    }
