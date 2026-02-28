from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.services.recommendation.path_generator import path_generator as pg
from app.schemas.recommendation import ConceptMasterySchema, Mission
from app.models.user import User

router = APIRouter()

@router.get("/next-mission", response_model=Mission)
def get_next_challenge(
    db: Session = Depends(deps.get_db_with_tenant),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Generate the next pedagogical mission based on gaps.
    """
    return pg.get_next_mission(db, current_user.id)

@router.get("/mastery", response_model=List[ConceptMasterySchema])
def get_mastery_graph(
    db: Session = Depends(deps.get_db_with_tenant),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    List all linguistic concepts and their mastery levels.
    """
    from sqlalchemy import select
    from app.models.knowledge import ConceptMastery
    return db.execute(select(ConceptMastery).where(ConceptMastery.user_id == current_user.id)).scalars().all()
