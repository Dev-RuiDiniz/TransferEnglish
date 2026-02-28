import io
from pydub import AudioSegment

class AudioSanitizer:
    """
    Ensures audio data stored or processed contains no sensitive metadata (EXIF/Tag stripping).
    Useful for LGPD/GDPR compliance.
    """

    @staticmethod
    def strip_metadata(audio_bytes: bytes, format: str = "wav") -> bytes:
        """
        Re-encodes audio to a raw format, effectively stripping any non-audio metadata tags.
        """
        try:
            audio = AudioSegment.from_file(io.BytesIO(audio_bytes), format=format)
            
            # Export to buffer without tags
            out_buffer = io.BytesIO()
            audio.export(out_buffer, format=format, tags={}) # Explicitly empty tags
            
            return out_buffer.getvalue()
        except Exception as e:
            # If stripping fails, return empty to be safe (fail-secure)
            print(f"Sanitization Error: {e}")
            return b""

audio_sanitizer = AudioSanitizer()
