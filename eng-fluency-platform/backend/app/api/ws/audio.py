from typing import List, Dict
from fastapi import WebSocket, WebSocketDisconnect
import json

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
        """
        try:
            while True:
                data = await websocket.receive()
                
                if "bytes" in data:
                    # Received binary audio chunk
                    audio_chunk = data["bytes"]
                    # Logically, we would send this to a processing queue (Celey)
                    # For now, just acknowledged
                    await websocket.send_json({
                        "type": "audio_ack",
                        "size": len(audio_chunk),
                        "status": "received"
                    })
                
                elif "text" in data:
                    # Received a control message
                    message = json.loads(data["text"])
                    if message.get("type") == "ping":
                        await websocket.send_json({"type": "pong"})
                    
        except WebSocketDisconnect:
            self.disconnect(websocket, tenant_id)

audio_manager = AudioSocketManager()
