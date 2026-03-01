from pydantic import BaseModel
from typing import Optional, List

class ConceptMasterySchema(BaseModel):
    concept_type: str
    concept_name: str
    mastery_score: float
    is_mastered: bool

    class Config:
        from_attributes = True

class Mission(BaseModel):
  title: str
  description: str
  target_focus: str
  concept_type: Optional[str] = None
