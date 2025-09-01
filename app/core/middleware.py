# app/core/middleware.py
from fastapi import Request
from fastapi.responses import JSONResponse
from datetime import datetime
from .logger import logger
from .error_codes import ERROR_CODES

async def global_middleware(request: Request, call_next):
    try:
        logger.info(f"Incoming request: {request.method} {request.url.path}")
        response = await call_next(request)
        logger.info(f"Response status: {response.status_code} for {request.url.path}")
        return response
    except Exception as exc:
        error_type = type(exc).__name__
        error_message = str(exc)

        # پیدا کردن کد خطا مرتبط (در صورت وجود)
        code = next((k for k, v in ERROR_CODES.items() if v == error_message), "GEN-000")
        
        logger.exception(f"Unhandled error: {error_type} - {error_message}")

        return JSONResponse(
            status_code=500,
            content={
                "timestamp": datetime.utcnow().isoformat(),
                "path": request.url.path,
                "code": code,
                "type": error_type,
                "message": error_message
            }
        )
