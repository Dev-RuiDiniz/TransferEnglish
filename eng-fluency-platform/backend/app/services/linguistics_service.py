from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.linguistics import Cognate, CognateType
from app.schemas.linguistics import CognateCreate, CognateUpdate
from typing import List, Optional

class LinguisticService:
    @staticmethod
    def get_cognates(
        db: Session, 
        skip: int = 0, 
        limit: int = 100,
        difficulty: Optional[str] = None,
        cognate_type: Optional[CognateType] = None
    ) -> List[Cognate]:
        query = select(Cognate)
        if difficulty:
            query = query.where(Cognate.difficulty_level == difficulty)
        if cognate_type:
            query = query.where(Cognate.type == cognate_type)
        
        return db.execute(query.offset(skip).limit(limit)).scalars().all()

    @staticmethod
    def create_cognate(db: Session, cognate_in: CognateCreate, tenant_id: str) -> Cognate:
        db_cognate = Cognate(
            **cognate_in.model_dump(),
            tenant_id=tenant_id
        )
        db.add(db_cognate)
        db.commit()
        db.refresh(db_cognate)
        return db_cognate

    @staticmethod
    def bulk_create_cognates(db: Session, cognates_list: List[dict], tenant_id: str):
        for data in cognates_list:
            db_cognate = Cognate(**data, tenant_id=tenant_id)
            db.add(db_cognate)
        db.commit()
