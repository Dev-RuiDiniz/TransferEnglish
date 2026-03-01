from pydantic import BaseModel
from typing import List, Optional

class PhonemeAssessment(BaseModel):
    phoneme: str
    accuracy_score: float

class WordPhoneticAssessment(BaseModel):
    word: str
    accuracy_score: float
    error_type: Optional[str] = None # None, Omission, Insertion, Mispronunciation
    phonemes: List[PhonemeAssessment]

class PhoneticAssessment(BaseModel):
    text: str
    accuracy_score: float # Overall accuracy
    fluency_score: float # Flow and rhythm
    prosody_score: float # Intonation
    completeness_score: float # How much of the target text was said
    words: List[WordPhoneticAssessment]
