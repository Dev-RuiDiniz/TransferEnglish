from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from app.api import deps
from app.models.analytics import FluencySession
from app.schemas.analytics import FluencySession as FluencySessionSchema, ProgressDashboard
from app.models.user import User

router = APIRouter()

@router.get("/me", response_model=ProgressDashboard)
def get_my_progress(
    db: Session = Depends(deps.get_db_with_tenant),
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get progress metrics for the current user.
    """
    sessions = db.execute(
        select(FluencySession)
        .where(FluencySession.user_id == current_user.id)
        .order_by(FluencySession.created_at.asc())
    ).scalars().all()

    if not sessions:
        return ProgressDashboard(
            current_ifp=0.0,
            sessions_count=0,
            fluency_evolution=[],
            weak_phonemes=[],
            strong_points=[]
        )

    return ProgressDashboard(
        current_ifp=sessions[-1].ifp_score,
        sessions_count=len(sessions),
        fluency_evolution=[s.ifp_score for s in sessions],
        weak_phonemes=["th", "r", "v"], # Placeholder
        strong_points=["Cognates usage", "Basic rhythm"] # Placeholder
    )

@router.get("/sessions", response_model=List[FluencySessionSchema])
def get_sessions(
    db: Session = Depends(deps.get_db_with_tenant),
    current_user: User = Depends(deps.get_current_user),
    limit: int = 10
) -> Any:
    return db.execute(
        select(FluencySession)
        .where(FluencySession.user_id == current_user.id)
        .order_by(FluencySession.created_at.desc())
        .limit(limit)
    ).scalars().all()
