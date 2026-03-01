import os
import io
import google.generativeai as genai
from pydub import AudioSegment
from app.core.config import settings
from app.schemas.audio import TranscriptionResult

class ASRService:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or settings.GOOGLE_API_KEY
        if self.api_key:
            genai.configure(api_key=self.api_key)
            # Use the specialized native audio model for best ASR results
            self.model = genai.GenerativeModel("gemini-2.5-flash-native-audio-latest")
        else:
            self.model = None

    def convert_to_wav(self, audio_bytes: bytes, format: str = "webm") -> io.BytesIO:
        """
        Convert incoming audio stream chunks (often webm) to MP3 for the model.
        """
        try:
            audio = AudioSegment.from_file(io.BytesIO(audio_bytes), format=format)
            buffer = io.BytesIO()
            audio.export(buffer, format="mp3")
            buffer.seek(0)
            return buffer
        except Exception as e:
            print(f"Audio conversion error: {e}")
            return io.BytesIO(audio_bytes) # Fallback

    async def transcribe(self, audio_buffer: io.BytesIO) -> TranscriptionResult:
        """
        Send audio to Google Gemini for transcription.
        """
        if not self.model:
            print("ASR Error: Google API Key not configured")
            return TranscriptionResult(text="")

        try:
            audio_data_bytes = audio_buffer.read()
            if not audio_data_bytes:
                return TranscriptionResult(text="")

            mime_type = "audio/mp3"
            if audio_data_bytes.startswith(b'\x1a\x45\xdf\xa3'):
                mime_type = "audio/webm"

            response = self.model.generate_content([
                {
                    "mime_type": mime_type,
                    "data": audio_data_bytes
                },
                "Transcription: "
            ])
            
            return TranscriptionResult(
                text=response.text.strip(),
                language="en"
            )
        except Exception as e:
            err_msg = str(e)
            if "API key not valid" in err_msg:
                print(f"CRITICAL: Gemini API Key is invalid or not activated. [DEBUG]: {err_msg}")
            elif "Quota" in err_msg or "429" in err_msg:
                print(f"WARNING: Gemini API Quota Exceeded. Please check your plan. [DEBUG]: {err_msg}")
            else:
                print(f"ASR (Gemini) Error (Full): {e}")
            return TranscriptionResult(text="")

asr_service = ASRService()
