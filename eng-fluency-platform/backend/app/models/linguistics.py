from sqlalchemy import String, Column, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base, TimestampMixin, TenantMixin
import enum
import uuid

class CognateType(str, enum.Enum):
    DIRECT = "direct"
    ADJUSTED = "adjusted"
    PARTIAL = "partial"
    FALSE = "false"

class Cognate(Base, TimestampMixin, TenantMixin):
    __tablename__ = "cognates"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    english_word: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    portuguese_word: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    type: Mapped[CognateType] = mapped_column(String(50), nullable=False)
    phonetic_transcription: Mapped[str] = mapped_column(String(255), nullable=True)
    example_sentence_en: Mapped[str] = mapped_column(String(500), nullable=True)
    example_sentence_pt: Mapped[str] = mapped_column(String(500), nullable=True)
    difficulty_level: Mapped[str] = mapped_column(String(10), default="A1") # CEFR levels
