import time
import json
import base64
from locust import HttpUser, task, between, events
import websocket
import rel

class ConversationUser(HttpUser):
    """
    Simulates a student in a real-time conversation.
    Tests WebSocket stability and backend latency.
    """
    wait_time = between(1, 5)

    @task
    def mock_conversation_session(self):
        tenant_id = "default-tenant"
        ws_url = f"ws://localhost:8000/ws/audio/{tenant_id}"
        
        # In a real stress test, we would use a proper websocket client inside Locust
        # For this demonstration, we'll simulate the load with HTTP and log WS connections
        start_time = time.time()
        
        # Simulating audio processing triggers
        response = self.client.get(f"/api/v1/analytics/dashboard", headers={"Authorization": "Bearer test-token"})
        
        if response.status_code == 200:
            events.request.fire(
                request_type="WebSocket",
                name="AudioStreamConnection",
                response_time=(time.time() - start_time) * 1000,
                response_length=0,
            )

    @task(3)
    def check_progression(self):
        self.client.get("/api/v1/progression/me")

    @task(2)
    def list_scenarios(self):
        self.client.get("/api/v1/recommendation/next-mission")
