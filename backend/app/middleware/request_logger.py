import time
import structlog
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

logger = structlog.get_logger(__name__)

class RequestLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        start = time.perf_counter()
        response = await call_next(request)
        elapsed_ms = (time.perf_counter() - start) * 1000

        logger.info(
            "http.request",
            method=request.method,
            path=request.url.path,
            url=str(request.url),
            status_code=response.status_code,
            elapsed_ms=round(elapsed_ms, 2),
            client_ip=request.client.host if request.client else "unknown",
        )

        return response