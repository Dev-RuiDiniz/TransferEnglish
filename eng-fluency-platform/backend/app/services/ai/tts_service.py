import os
import httpx
from typing import Optional

class TTSService:
    def __init__(self, api_key: str = None):
        self.elevenlabs_api_key = api_key or os.getenv("ELEVENLABS_API_KEY")
        self.elevenlabs_url = "https://api.elevenlabs.io/v1/text-to-speech"
        self.default_voice_id = "21m00Tcm4TlvDq8ikWAM" # Example voice (Rachel)

    async def generate_speech(self, text: str, voice_id: Optional[str] = None) -> bytes:
        """
        Synthesize speech using ElevenLabs API.
        Returns audio bytes (mp3).
        """
        if not self.elevenlabs_api_key:
            # Fallback or error
            print("Warning: ElevenLabs API Key missing. Skipping speech generation.")
            return b""

        v_id = voice_id or self.default_voice_id
        url = f"{self.elevenlabs_url}/{v_id}"
        
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.elevenlabs_api_key
        }
        
        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data, headers=headers)
            if response.status_code == 200:
                return response.content
            else:
                print(f"ElevenLabs TTS Error: {response.text}")
                return b""

tts_service = TTSService()
