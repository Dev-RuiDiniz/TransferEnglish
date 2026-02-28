from pydantic import BaseModel
from typing import Optional
from app.models.linguistics import CognateType

class CognateBase(BaseModel):
    english_word: str
    portuguese_word: str
    type: CognateType
    phonetic_transcription: Optional[str] = None
    example_sentence_en: Optional[str] = None
    example_sentence_pt: Optional[str] = None
    difficulty_level: str = "A1"

class CognateCreate(CognateBase):
    pass

class CognateUpdate(CognateBase):
    english_word: Optional[str] = None
    portuguese_word: Optional[str] = None
    type: Optional[CognateType] = None

class Cognate(CognateBase):
    id: str
    tenant_id: str

    class Config:
        from_attributes = True

class ScenarioBase(BaseModel):
    title: str
    description: Optional[str] = None
    config: dict
    level: str = "intermediate"

class Scenario(ScenarioBase):
    id: str

    class Config:
        from_attributes = True
