# app/cache/cache_service.py
import json
from app.cache.redis import redis_client

DEFAULT_TTL = 1200  # 20 minutes

async def get(key: str):
    data = await redis_client.get(key)
    if data:
        return json.loads(data)
    return None

async def set(key: str, value, ttl: int = DEFAULT_TTL):
    await redis_client.set(key, json.dumps(value), ex=ttl)

async def delete(key: str):
    await redis_client.delete(key)