import logging
import re
import sys

import structlog

API_KEY_PATTERN = re.compile(r"(api_key=)([^&\s]+)", re.IGNORECASE)

def sanitize_url(url: str) -> str:
    return API_KEY_PATTERN.sub(r"\1****", url)

def sanitize_event(logger, method_name, event_dict):
    if "url" in event_dict:
        event_dict["url"] = sanitize_url(event_dict["url"])
    return event_dict

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

structlog.configure(
    processors=[
        sanitize_event,
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)