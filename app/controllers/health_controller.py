from sqlalchemy.orm import Session

from app.services import health_service


def health(db: Session) -> dict:
    """Controller: takes the request, calls the service, returns the response."""
    return health_service.get_health(db)
