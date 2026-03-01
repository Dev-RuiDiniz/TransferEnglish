import os
import io
from gtts import gTTS
from typing import Optional
from app.core.config import settings

class TTSService:
    def __init__(self, api_key: str = None):
        self.google_api_key = api_key or settings.GOOGLE_API_KEY
        # In a production environment, we'd use the Gemini 2.5 TTS model
        # but for now, gTTS provides the immediate audio response requested by the user.
        print("LuckArkman Voice Engine v2.5 initialized with gTTS fallback.")

    async def generate_speech(self, text: str, voice_id: Optional[str] = None, settings: Optional[dict] = None) -> bytes:
        """
        Synthesize speech from text using Google TTS.
        Returns audio bytes (mp3).
        """
        if not text:
            return b""

        try:
            # We use English (en) by default as the tutor is an English speaker
            tts = gTTS(text=text, lang='en', slow=False)
            
            # Save to a byte buffer
            buffer = io.BytesIO()
            tts.write_to_fp(buffer)
            buffer.seek(0)
            
            audio_data = buffer.read()
            if audio_data:
                print(f"TTS: Generated {len(audio_data)} bytes of audio for: '{text[:30]}...'")
            return audio_data

        except Exception as e:
            print(f"LuckArkman Voice Error (gTTS): {e}")
            return b""

tts_service = TTSService()
