

```markdown
# 🚀 FastAPI Error Handling & Logging – Three-Layer Architecture Example

[🇮🇷 نسخه فارسی ⬇](#-نمونه-معماری-سه-لایه--مدیریت-خطا-و-لاگینگ)

![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-%2300b894?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.10%2B-%233776AB?logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A sample **FastAPI** project demonstrating:
- Advanced error handling (Custom Exceptions + Global Middleware)
- Professional logging (`RotatingFileHandler` + structured output)
- Three-layer architecture (API → Service → Repository)
- Standardized input/output modeling with **Pydantic**
- Suitable for use as a **Portfolio project** on GitHub



## 📂 Project Structure

```
app/

  ├── api/                # API layer (routes/endpoints)
  │   ├── error_codes.py

  │   └── user_routes.py
  ├── core/               # Core configurations
  │   ├── error_codes.py

  │   ├── logger.py

  │   └── middleware.py

  ├── models/             # Pydantic models
  │   └── user_models.py

  ├── repositories/       # Data access layer
  │   └── user_repository.py

  ├── services/           # Business logic layer
  │   └── user_service.py

  └── main.py             # Application entry point
```



## ⚡ Features

- **Global Error Handling**  
  All errors are returned in a standardized JSON format (error code, message, timestamp).
- **Advanced Logging**  
  Uses `RotatingFileHandler` for log file rotation and full traceback logging.
- **Exception Chaining**  
  Preserve original exceptions for better debugging.
- **Three-Layer Structure**  
  Complete separation of API, business logic, and data access for scalability.
- **Full Swagger/OpenAPI Coverage**  
  Pydantic models with `example` fields for auto-generated, rich documentation.



## 📦 Installation & Run

### 1. Clone repo
```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>
```

### 2. Virtual environment & dependencies
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run server
```bash
uvicorn app.main:app --reload
```

### 4. Test in browser
- Swagger docs:  
  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- Example endpoints:  
  - `/users/1` → existing data  
  - `/users/999` → structured error  
  - `/error-codes` → list of all error codes



## 📄 Sample Error Response
```json
{
  "error_code": "USER_NOT_FOUND",
  "detail": "User not found",
  "timestamp": "2025-09-01T18:20:00Z"
}
```



## 🗄 Logs
- Path: `logs/app.log`
- Example:
```
2025-09-01 18:20:00,123 [INFO] Service: fetching details for user ID 999
2025-09-01 18:20:00,125 [ERROR] 404 - User not found (User ID: 999)
Traceback (most recent call last):
  ...
```



## 🛠 Tech Stack
- [FastAPI](https://fastapi.tiangolo.com)
- [Pydantic](https://docs.pydantic.dev)
- [Uvicorn](https://www.uvicorn.org)
- Python Logging







# 📚 نمونه معماری سه‌لایه – مدیریت خطا و لاگینگ در FastAPI

[English Version ⬆](#fastapi-error-handling--logging--three-layer-architecture-example)

یک پروژه نمونه **FastAPI** برای نمایش:
- مدیریت خطای پیشرفته (Custom Exceptions + Global Middleware)
- لاگینگ حرفه‌ای (`RotatingFileHandler` + خروجی ساختاریافته)
- معماری سه‌لایه (API → Service → Repository)
- مدل‌سازی استاندارد ورودی/خروجی با **Pydantic**
- قابلیت استفاده به عنوان **نمونه کار فنی** در GitHub



## 📂 ساختار پروژه

```
app/
  ├── api/                # لایه API (مسیرها)
  ├── core/               # پیکربندی‌ها
  ├── models/             # مدل‌های Pydantic
  ├── repositories/       # لایه داده
  ├── services/           # لایه بیزینس
  └── main.py              # نقطه ورود
```



## ⚡ ویژگی‌ها

- **مدیریت خطای سراسری** با فرمت JSON استاندارد
- **لاگینگ پیشرفته** با چرخش فایل (Rolling Logs)
- **Exception Chaining** برای حفظ خطای اصلی
- **معماری سه‌لایه** برای توسعه‌پذیری بیشتر
- **اتصال کامل به Swagger/OpenAPI** با مثال‌ها



## 📦 نصب و اجرا

```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>
python -m venv venv
source venv/bin/activate   # ویندوز: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)



## 📄 نمونه خروجی خطا

```json
{
  "error_code": "USER_NOT_FOUND",
  "detail": "User not found",
  "timestamp": "2025-09-01T18:20:00Z"
}
```



## 🗄 مسیر لاگ‌ها
`logs/app.log`



## 🛠 تکنولوژی‌ها
- FastAPI
- Pydantic
- Uvicorn
- Python Logging

