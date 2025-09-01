# app/repositories/user_repository.py

# شبیه‌سازی دیتابیس
FAKE_USERS_DB = {
    1: {"id": 1, "name": "John Doe"},
    2: {"id": 2, "name": "Jane Smith"},
}

def get_user_by_id(user_id: int):
    """
    جستجو کاربر بر اساس ID
    """
    return FAKE_USERS_DB.get(user_id)
