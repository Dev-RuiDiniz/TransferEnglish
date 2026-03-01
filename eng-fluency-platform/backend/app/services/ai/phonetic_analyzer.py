import os
import azure.cognitiveservices.speech as speechsdk
from app.schemas.phonetic import PhoneticAssessment, WordPhoneticAssessment, PhonemeAssessment

class PhoneticAnalyzer:
    def __init__(self, subscription_key: str = None, region: str = None):
        self.speech_config = speechsdk.SpeechConfig(
            subscription=subscription_key or os.getenv("AZURE_SPEECH_KEY"),
            region=region or os.getenv("AZURE_SPEECH_REGION")
        )

    async def analyze_pronunciation(self, audio_path: str, reference_text: str) -> PhoneticAssessment:
        """
        Analyzes audio against a reference text using Azure Pronunciation Assessment.
        """
        audio_config = speechsdk.audio.AudioConfig(filename=audio_path)
        
        # Configure Pronunciation Assessment
        pronunciation_config = speechsdk.PronunciationAssessmentConfig(
            reference_text=reference_text,
            grading_system=speechsdk.PronunciationAssessmentGradingSystem.HundredMark,
            granularity=speechsdk.PronunciationAssessmentGranularity.Phoneme,
            enable_prosody_assessment=True
        )

        speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config, 
            audio_config=audio_config
        )
        
        pronunciation_config.apply_to(speech_recognizer)
        
        # Process result
        result = speech_recognizer.recognize_once_async().get()
        
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            pa_result = speechsdk.PronunciationAssessmentResult(result)
            
            words = []
            for w in pa_result.words:
                phonemes = []
                if w.phonemes:
                    for p in w.phonemes:
                        phonemes.append(PhonemeAssessment(
                            phoneme=p.phoneme,
                            accuracy_score=p.accuracy_score
                        ))
                
                words.append(WordPhoneticAssessment(
                    word=w.word,
                    accuracy_score=w.accuracy_score,
                    error_type=w.error_type,
                    phonemes=phonemes
                ))

            return PhoneticAssessment(
                text=result.text,
                accuracy_score=pa_result.accuracy_score,
                fluency_score=pa_result.fluency_score,
                prosody_score=pa_result.prosody_score,
                completeness_score=pa_result.completeness_score,
                words=words
            )
        else:
            # Handle error case
            return PhoneticAssessment(
                text="", accuracy_score=0, fluency_score=0, 
                prosody_score=0, completeness_score=0, words=[]
            )

# Instance with default env vars
phonetic_analyzer = PhoneticAnalyzer()
