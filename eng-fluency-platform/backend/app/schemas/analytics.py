from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class FluencySessionBase(BaseModel):
    ifp_score: float
    accuracy_avg: float
    fluency_avg: float
    prosody_avg: float
    total_words: int
    duration_seconds: float
    response_latency_avg: float

class FluencySessionCreate(FluencySessionBase):
    user_id: str
    session_data: Optional[dict] = None

class FluencySession(FluencySessionBase):
    id: str
    tenant_id: str
    created_at: datetime

    class Config:
        from_attributes = True

class ProgressDashboard(BaseModel):
    current_ifp: float
    sessions_count: int
    fluency_evolution: List[float]
    weak_phonemes: List[str]
    strong_points: List[str]
