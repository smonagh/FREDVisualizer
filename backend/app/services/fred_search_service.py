import httpx

from app.env import SEARCH_URL, FRED_API_KEY
from app.cache.cache_service import get, set
from app.cache.keys import fred_observations_key

async def get_search(query: str):
    """Get series id back from search query"""

    cache_key = fred_observations_key(query)
    cached = await get(cache_key)
    if cached:
        return cached
    
    params = {
        "search_text": query,
        "api_key": FRED_API_KEY,
        "file_type": "json"
    }
    async with httpx.AsyncClient() as client:
        res = await client.get(SEARCH_URL, params=params)
        data = res.json()
        series = data.get("seriess", [])
        
        # Only pull the first 5 search results to limit data
        await set(cache_key, series[0:5], ttl=1200)
        return series[0:5]