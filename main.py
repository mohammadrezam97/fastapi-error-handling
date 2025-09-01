# main.py
from fastapi import FastAPI
from app.api import error_codes, user_routes
from app.core.middleware import global_middleware

app = FastAPI(
    title="FastAPI Enterprise Error Handling",
    version="1.0.0"
)

# Middleware را ثبت کنیم
app.middleware("http")(global_middleware)

# Routerها
app.include_router(error_codes.router)
app.include_router(user_routes.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Enterprise Error Handling"}
