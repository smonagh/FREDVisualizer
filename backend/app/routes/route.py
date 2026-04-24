from fastapi import APIRouter
from fastapi_cache.decorator import cache

from redis.exceptions import RedisError
from fastapi import HTTPException

from app.services.fred_series_service import get_series
from app.services.fred_search_service import get_search
from app.cache.redis import redis_client

router = APIRouter()

@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.get("/health")
async def health():
    try:
        await redis_client.ping()
        return {
            "status": "ok",
            "service": "FREDVisualizer",
            "cache": "connected"
        }
    except RedisError:
        raise HTTPException(status_code=503, detail="Redis unavailable")

@cache(expire=300)
@router.get("/series/{identifier}")
async def read_series(identifier: str):
    data = await get_series(identifier)
    return {"data": data}

@cache(expire=300)
@router.get("/search/{query}")
async def read_search(query: str):
    data = await get_search(query)
    return {"data": data}