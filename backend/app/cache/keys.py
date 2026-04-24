

def fred_series_key(series_id: str) -> str:
    return f"fred:series:{series_id}"

def fred_observations_key(series_id: str) -> str:
    return f"fred:observations:{series_id}"