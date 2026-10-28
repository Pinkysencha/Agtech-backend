from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.database import check_connection
from app.config.settings import settings
from app.middleware.error_handlers import register_error_handlers
from app.middleware.request_logging import log_requests, setup_logging
from app.routes import demo, health

setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        check_connection()
        print("Database connected")
    except Exception as e:
        print(f"Database connection FAILED: {e}")
    yield


app = FastAPI(title="AgTech API", lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)


app.middleware("http")(log_requests)

register_error_handlers(app)


app.include_router(health.router)
app.include_router(demo.router)


@app.get("/")
def root():
    return {"message": "AgTech API running"}