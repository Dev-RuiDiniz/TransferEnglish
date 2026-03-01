from sqlalchemy import String, Integer, Float, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base, TimestampMixin, TenantMixin
import enum
import uuid

class CEFRLevel(str, enum.Enum):
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"

class UserLevel(Base, TimestampMixin, TenantMixin):
    __tablename__ = "user_levels"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), unique=True, index=True)
    
    current_level: Mapped[CEFRLevel] = mapped_column(String(2), default=CEFRLevel.A1)
    
    # Proficiency breakdown (0-100)
    speaking_score: Mapped[float] = mapped_column(Float, default=0.0)
    listening_score: Mapped[float] = mapped_column(Float, default=0.0)
    pronunciation_score: Mapped[float] = mapped_column(Float, default=0.0)
    vocabulary_score: Mapped[float] = mapped_column(Float, default=0.0)
    
    # Experience points / Progress toward next level
    total_xp: Mapped[int] = mapped_column(Integer, default=0)
    level_progress: Mapped[float] = mapped_column(Float, default=0.0) # 0.0 to 1.0 within current level
