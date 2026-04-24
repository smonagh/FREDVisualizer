import httpx
import datetime
import logging

from app.env import SERIES_URL, FRED_API_KEY
from app.cache.cache_service import get, set
from app.cache.keys import fred_series_key

logger = logging.getLogger(__name__)

async def get_series(series_id: str):
    """Get series data"""

    cache_key = fred_series_key(series_id)
    cached = await get(cache_key)
    if cached:
        return cached
    
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json"
    }
    async with httpx.AsyncClient() as client:
        res = await client.get(SERIES_URL, params=params)
        if res.status_code != 200:
            return []
        else:
            try:
                await set(cache_key, res.json(), ttl=600)
            except Exception as e:
                logger.error(f"Error occurred while setting cache: {e}")

        data = res.json()
        observations = data.get("observations", [])
        if not observations:
            return observations
        
        processed_data = process_observations(observations)
        return processed_data

def process_observations(observations: list):
    """Process observations according the FRED spec"""
    
    observation_list = []
    for obs in observations:
        if not obs.get("date") or not obs.get("value"):
            continue

        date_val = get_date_value(obs["date"])
        numeric_val = get_numeric_value(obs["value"])

        if not date_val and not numeric_val:
            continue

        observation_list.append({"date": date_val, "value": numeric_val})
    
    sorted_data = sorted(observation_list, key=lambda x: x["date"])
    return sorted_data

def get_date_value(input_value: str):
    """Get date value from string and return None otherwise"""

    try:
        date_val = datetime.datetime.strptime(input_value, "%Y-%m-%d").date()
    except ValueError:
        date_val = None

    return date_val

def get_numeric_value(input_value: str):
    """Get numeric value from string and return None otherwise"""

    try:
        numeric_val = float(input_value)
    except ValueError:
        numeric_val = None

    return numeric_val