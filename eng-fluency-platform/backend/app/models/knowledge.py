from sqlalchemy import String, Float, Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base, TimestampMixin, TenantMixin
import uuid

class ConceptMastery(Base, TimestampMixin, TenantMixin):
    """
    Tracks the performance and level of mastery of a specific linguistic concept
    (phoneme, grammatical rule, or vocabulary cluster) for a user.
    """
    __tablename__ = "concept_mastery"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), index=True)
    
    concept_type: Mapped[str] = mapped_column(String(50)) # e.g., 'phoneme', 'cognate', 'grammar'
    concept_name: Mapped[str] = mapped_column(String(100)) # e.g., 'th-sound', 'cognate-transfer'
    
    mastery_score: Mapped[float] = mapped_column(Float, default=0.0) # 0 to 100
    errors_count: Mapped[int] = mapped_column(Integer, default=0)
    success_count: Mapped[int] = mapped_column(Integer, default=0)
    
    is_mastered: Mapped[bool] = mapped_column(Boolean, default=False)
    last_practiced: Mapped[str] = mapped_column(String, nullable=True) # Timestamp ISO
