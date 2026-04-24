import redis.asyncio as redis
from app.env import REDIS_URL

redis_client = redis.from_url(REDIS_URL, decode_responses=True)