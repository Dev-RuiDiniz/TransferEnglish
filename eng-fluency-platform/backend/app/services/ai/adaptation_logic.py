from typing import Dict, Any, List
from app.schemas.analytics import FluencySessionBase

class AdaptationLogic:
    """
    Adjusts the conversation difficulty dynamically based on user performance.
    """

    @staticmethod
    def update_metrics(current: FluencySessionBase, transcription: Any) -> FluencySessionBase:
        """
        Updates session metrics based on recent transcription.
        In a real app, this would use PhoneticAnalyzer results.
        For now, we'll simulate a slight improvement/decline based on text length and confidence.
        """
        # Simple simulation: longer texts increase complexity/IFP
        word_count = len(transcription.text.split())
        current.total_words += word_count
        
        # Simulated IFP adjustment
        if word_count > 10:
            current.ifp_score = min(100.0, current.ifp_score + 1.0)
        elif word_count < 3:
            current.ifp_score = max(0.0, current.ifp_score - 1.0)
            
        return current

    @staticmethod
    def get_tts_config(session_metrics: FluencySessionBase) -> Dict[str, Any]:
        """
        Returns ElevenLabs or OpenAI TTS settings.
        Stability and clarity for lower scores, natural speed for higher.
        """
        ifp = session_metrics.ifp_score
        
        if ifp < 40:
            return {"stability": 0.8, "similarity_boost": 0.5, "speed": 0.85}
        elif ifp > 80:
            return {"stability": 0.4, "similarity_boost": 0.8, "speed": 1.1}
        
        return {"stability": 0.5, "similarity_boost": 0.75, "speed": 1.0}

    @staticmethod
    def get_llm_instruction(session_metrics: FluencySessionBase) -> str:
        """
        Returns a system prompt modifier to adjust vocabulary complexity.
        """
        ifp = session_metrics.ifp_score
        
        if ifp < 40:
            return "Use simpler words and short sentences. Avoid complex idioms. Speak slightly slower."
        elif ifp > 75:
            return "Use advanced business vocabulary and natural idioms. Challenge the user with slightly faster pacing."
            
        return "Keep a natural but clear pedagogical tone."

adaptation_logic = AdaptationLogic()
