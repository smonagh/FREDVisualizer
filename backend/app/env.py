import os
from dotenv import load_dotenv

load_dotenv()
SERIES_URL = "https://api.stlouisfed.org/fred/series/observations"
SEARCH_URL = "https://api.stlouisfed.org/fred/series/search"
FRED_API_KEY = os.getenv("FRED_API_KEY")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
if FRED_API_KEY is None:
    raise EnvironmentError("Failed because FRED_API_KEY is not set.")