from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.services.progression_service import progression_service
from app.schemas.progression import UserLevel
from app.models.user import User

router = APIRouter()

@router.get("/me", response_model=UserLevel)
def get_my_level(
    db: Session = Depends(deps.get_db_with_tenant),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get current user's CEFR level and proficiency scores.
    """
    return progression_service.get_user_level(db, current_user.id)
