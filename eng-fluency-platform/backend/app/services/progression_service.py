from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.progression import UserLevel, CEFRLevel
from app.schemas.progression import UserLevelUpdate
from typing import Optional

class ProgressionService:
    @staticmethod
    def get_user_level(db: Session, user_id: str) -> UserLevel:
        query = select(UserLevel).where(UserLevel.user_id == user_id)
        level = db.execute(query).scalar_one_or_none()
        
        if not level:
            # Initialize level if it doesn't exist
            level = UserLevel(user_id=user_id)
            db.add(level)
            db.commit()
            db.refresh(level)
        return level

    @staticmethod
    def update_progress(db: Session, user_id: str, update: UserLevelUpdate) -> UserLevel:
        level = ProgressionService.get_user_level(db, user_id)
        
        if update.speaking_score is not None:
            level.speaking_score = (level.speaking_score + update.speaking_score) / 2
        if update.listening_score is not None:
            level.listening_score = (level.listening_score + update.listening_score) / 2
        if update.pronunciation_score is not None:
            level.pronunciation_score = (level.pronunciation_score + update.pronunciation_score) / 2
        
        if update.xp_gain:
            level.total_xp += update.xp_gain
            # Simple level up logic: every 1000 XP increases progress by 20%
            level.level_progress += (update.xp_gain / 5000)
            
            if level.level_progress >= 1.0:
                ProgressionService._level_up(level)
        
        db.commit()
        db.refresh(level)
        return level

    @staticmethod
    def _level_up(level: UserLevel):
        levels = list(CEFRLevel)
        current_idx = levels.index(level.current_level)
        if current_idx < len(levels) - 1:
            level.current_level = levels[current_idx + 1]
            level.level_progress = 0.0
            print(f"User {level.user_id} leveled up to {level.current_level}!")

progression_service = ProgressionService()
