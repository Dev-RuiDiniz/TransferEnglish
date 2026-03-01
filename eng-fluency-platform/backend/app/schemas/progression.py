from pydantic import BaseModel
from app.models.progression import CEFRLevel
from typing import Optional, List

class UserLevelBase(BaseModel):
    current_level: CEFRLevel
    speaking_score: float
    listening_score: float
    pronunciation_score: float
    vocabulary_score: float
    total_xp: int
    level_progress: float

class UserLevelUpdate(BaseModel):
    speaking_score: Optional[float] = None
    listening_score: Optional[float] = None
    pronunciation_score: Optional[float] = None
    vocabulary_score: Optional[float] = None
    xp_gain: Optional[int] = None

class UserLevel(UserLevelBase):
    user_id: str

    class Config:
        from_attributes = True

class LevelUp(BaseModel):
    old_level: CEFRLevel
    new_level: CEFRLevel
    message: str
