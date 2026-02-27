from sqlalchemy import String, Float, Integer, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base, TimestampMixin, TenantMixin
import uuid

class FluencySession(Base, TimestampMixin, TenantMixin):
    __tablename__ = "fluency_sessions"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"), index=True)
    
    # Metrics
    ifp_score: Mapped[float] = mapped_column(Float, default=0.0) # Index of Fluency under Pressure
    accuracy_avg: Mapped[float] = mapped_column(Float, default=0.0)
    fluency_avg: Mapped[float] = mapped_column(Float, default=0.0)
    prosody_avg: Mapped[float] = mapped_column(Float, default=0.0)
    
    # Timing and counts
    total_words: Mapped[int] = mapped_column(Integer, default=0)
    duration_seconds: Mapped[float] = mapped_column(Float, default=0.0)
    response_latency_avg: Mapped[float] = mapped_column(Float, default=0.0)
    
    # Detailed logs (stored as JSON)
    session_data: Mapped[dict] = mapped_column(JSON, nullable=True)
