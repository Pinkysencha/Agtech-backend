from sqlalchemy import text
from sqlalchemy.orm import Session


def get_health(db: Session) -> dict:
    """Business logic: is the API up, and can it reach the database?"""
    try:
        db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception:
        db_status = "unreachable"
    return {"status": "ok", "database": db_status}
