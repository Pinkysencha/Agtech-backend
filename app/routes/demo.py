from fastapi import APIRouter
from app.schemas.auth import RegisterRequest

router = APIRouter(prefix="/_demo", tags=["demo"])


@router.post("/signup")
def signup(body: RegisterRequest):
    return {"ok": True, "name": body.name}