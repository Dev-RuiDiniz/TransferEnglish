from fastapi import WebSocket, WebSocketDisconnect
import json
import base64
import time
import io
from app.services.ai.asr_service import asr_service
from app.services.ai.chat_service import chat_service
from app.services.ai.tts_service import tts_service
from app.services.ai.adaptation_logic import adaptation_logic
from app.services.ai.interruption_engine import interruption_engine
from app.services.ai.pressure_engine import pressure_engine
from typing import Dict, List
from app.models.fluency_session import FluencySessionBase

class AudioSocketManager:
    def __init__(self):
        # active_connections maps tenant_id to a list of sockets
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, tenant_id: str):
        await websocket.accept()
        if tenant_id not in self.active_connections:
            self.active_connections[tenant_id] = []
        self.active_connections[tenant_id].append(websocket)

    def disconnect(self, websocket: WebSocket, tenant_id: str):
        if tenant_id in self.active_connections:
            self.active_connections[tenant_id].remove(websocket)
            if not self.active_connections[tenant_id]:
                del self.active_connections[tenant_id]

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast_to_tenant(self, message: str, tenant_id: str):
        if tenant_id in self.active_connections:
            for connection in self.active_connections[tenant_id]:
                await connection.send_text(message)

    async def handle_audio_stream(self, websocket: WebSocket, tenant_id: str):
        """
        Main loop for handling binary audio data and control messages.
        Orchestrates the full cycle: User Audio -> Transcription -> LLM -> TTS -> Client
        """
        conversation_history = []
    
        # Session tracking for adaptation (Sprint 16)
        session_metrics = FluencySessionBase(
            ifp_score=60.0, # Initial "Functional" baseline
            accuracy_avg=70.0,
            fluency_avg=70.0,
            prosody_avg=70.0,
            total_words=0,
            duration_seconds=0.0,
            response_latency_avg=1.0
        )
    
        try:
            while True:
                data = await websocket.receive()
                
                if "bytes" in data:
                    # 1. Received binary audio chunk
                    start_time = time.time()
                    audio_chunk = data["bytes"]
                    
                    # 2. Transcription (ASR)
                    # Convert to proper buffer format
                    audio_buffer = asr_service.convert_to_wav(audio_chunk)
                    transcription = await asr_service.transcribe(audio_buffer)
                    
                    if not transcription.text.strip():
                        continue

                    # 3. Interruption Check (Pedagogical tips)
                    tip = await interruption_engine.analyze(transcription.text)
                    if tip:
                        await websocket.send_json({
                            "type": "quick_tip",
                            "data": tip
                        })

                    # Update session metrics based on transcription
                    session_metrics = adaptation_logic.update_metrics(session_metrics, transcription)

                    # 4. Dynamic Adaptation (Sprint 16)
                    system_mod = adaptation_logic.get_llm_instruction(session_metrics)
                    tts_settings = adaptation_logic.get_tts_config(session_metrics)

                    await websocket.send_json({
                        "type": "transcription",
                        "text": transcription.text
                    })

                    # 4. AI Logic (Chat)
                    ai_response_text = await chat_service.get_response(
                        conversation_history, 
                        transcription.text,
                        system_modifier=system_mod
                    )
                    
                    # Update history
                    conversation_history.append({"role": "user", "content": transcription.text})
                    conversation_history.append({"role": "assistant", "content": ai_response_text})

                    # 5. Voice Synthesis (TTS)
                    audio_response = await tts_service.generate_speech(
                        ai_response_text,
                        settings=tts_settings
                    )

                    # Send responses
                    await websocket.send_json({
                        "type": "ai_response",
                        "text": ai_response_text
                    })
                    
                    if audio_response:
                        await websocket.send_json({
                            "type": "audio_response",
                            "audio": base64.b64encode(audio_response).decode('utf-8')
                        })

                    # 5. Potential Pressure Mode Trigger (20% chance)
                    import random
                    if random.random() < 0.2:
                        challenge = pressure_engine.trigger_challenge()
                        await websocket.send_json({
                            "type": "pressure_challenge",
                            "data": challenge.model_dump()
                        })
                
                elif "text" in data:
                    message = json.loads(data["text"])
                    if message.get("type") == "ping":
                        await websocket.send_json({"type": "pong"})
                    elif message.get("type") == "clear_history":
                        conversation_history = []
                    
        except WebSocketDisconnect:
            self.disconnect(websocket, tenant_id)

audio_manager = AudioSocketManager()
