from sqlalchemy import String, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base, TimestampMixin
import uuid

class ScenarioTemplate(Base, TimestampMixin):
    """
    Templates for advanced conversation scenarios (interviews, debates, storytelling).
    """
    __tablename__ = "scenario_templates"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    
    # JSON structure defining the persona, system prompt, and starting lines
    # Example: {"persona": "CEO", "tone": "formal", "objectives": ["negotiate salary"]}
    config: Mapped[dict] = mapped_column(JSON, nullable=False)
    
    # Difficulty tags or levels
    level: Mapped[str] = mapped_column(String(50), default="intermediate")
