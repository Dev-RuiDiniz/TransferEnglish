from typing import Any, List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.services.linguistics_service import LinguisticService
from app.schemas.linguistics import Cognate, CognateType

router = APIRouter()

@router.get("/cognates", response_model=List[Cognate])
def read_cognates(
    db: Session = Depends(deps.get_db_with_tenant),
    skip: int = 0,
    limit: int = 100,
    difficulty: Optional[str] = None,
    type: Optional[CognateType] = None
) -> Any:
    """
    Retrieve cognates with filtering.
    """
    return LinguisticService.get_cognates(
        db, skip=skip, limit=limit, difficulty=difficulty, cognate_type=type
    )
