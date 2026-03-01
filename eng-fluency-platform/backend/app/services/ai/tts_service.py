import os
import google.generativeai as genai
from typing import Optional
from app.core.config import settings

class TTSService:
    def __init__(self, api_key: str = None):
        self.google_api_key = api_key or settings.GOOGLE_API_KEY
        if self.google_api_key:
            genai.configure(api_key=self.google_api_key)
            self.model_name = "gemini-2.5-flash-native-audio-latest"
        else:
            self.model_name = None

    async def generate_speech(self, text: str, voice_id: Optional[str] = None, settings: Optional[dict] = None) -> bytes:
        """
        Synthesize speech using Google Gemini TTS API.
        Returns audio bytes (wav/mp3).
        """
        if not self.google_api_key:
            print("Warning: GOOGLE_API_KEY missing. Skipping speech generation.")
            return b""

        try:
            model = genai.GenerativeModel(self.model_name)
            # Use specific response_mime_type to get audio output
            response = model.generate_content(
                text,
                generation_config=genai.types.GenerationConfig(
                    response_mime_type="audio/wav"
                )
            )
            
            # Extract audio from response parts
            for part in response.candidates[0].content.parts:
                if part.inline_data and part.inline_data.data:
                    return part.inline_data.data
            
            return b""
        except Exception as e:
            print(f"Gemini TTS Error: {e}")
            return b""

tts_service = TTSService()
