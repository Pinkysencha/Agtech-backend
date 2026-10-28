from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.database import check_connection
from app.config.settings import settings
from app.routes import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        check_connection()
        print("Database connected")
    except Exception as e:
        print(f"Database connection FAILED: {e}")
    yield


app = FastAPI(title="AgTech API", lifespan=lifespan)

# CORS: lets the React dev server call this API from the browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(health.router)


@app.get("/")
def root():
    return {"message": "AgTech API running"}
