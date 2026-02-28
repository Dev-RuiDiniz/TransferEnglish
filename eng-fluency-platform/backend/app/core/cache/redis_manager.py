import redis
import os
import json
from typing import Optional, Any
from datetime import timedelta

class CacheManager:
    """
    Handles caching for expensive operations like LLM responses, 
    phonetic analysis results, and shared tenant data.
    """
    def __init__(self):
        redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
        self.client = redis.from_url(redis_url)

    def get(self, key: str) -> Optional[Any]:
        """Retrieve data from cache."""
        data = self.client.get(key)
        if data:
            return json.loads(data)
        return None

    def set(self, key: str, value: Any, expire_seconds: int = 3600):
        """Store data in cache with an expiration time."""
        self.client.setex(
            key,
            expire_seconds,
            json.dumps(value)
        )

    def delete(self, key: str):
        """Remove a specific key from cache."""
        self.client.delete(key)

    def clear_tenant_cache(self, tenant_id: str):
        """Clear all cached entries matching a tenant pattern."""
        keys = self.client.keys(f"tenant:{tenant_id}:*")
        if keys:
            self.client.delete(*keys)

cache_manager = CacheManager()
