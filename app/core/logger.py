# app/core/logger.py
import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = os.path.join(os.path.dirname(__file__), "../../logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, "app.log")

# ایجاد لاگر اصلی
logger = logging.getLogger("fastapi_app")
logger.setLevel(logging.INFO)

# هندلر برای فایل با rotation
file_handler = RotatingFileHandler(
    LOG_FILE_PATH, maxBytes=5_000_000, backupCount=5, encoding="utf-8"
)
file_handler.setLevel(logging.INFO)

# هندلر برای کنسول
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# فرمت مشترک
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] [%(name)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# اضافه کردن هندلرها
logger.addHandler(file_handler)
logger.addHandler(console_handler)
