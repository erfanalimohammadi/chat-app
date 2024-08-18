import time
from collections import defaultdict
from fastapi import Request, Response
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint,
)
from starlette.types import ASGIApp
from App.config.logs import logger  


class RequestLimitMiddleware(BaseHTTPMiddleware):
    def __init__(
        self, app: ASGIApp, max_requests: int = 4, window_seconds: int = 1
    ):
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.request_history: dict[str, tuple[int, float]] = defaultdict(
            lambda: (0, 0.0)
        )

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        client_ip = request.client.host if request.client else "unknown"
        current_time = time.time()

        
        logger.info(f"Received request from {client_ip} at {current_time}")

        
        count, last_request_time = self.request_history[client_ip]

        
        if current_time - last_request_time > self.window_seconds:
            count = 0

        
        count += 1

        
        self.request_history[client_ip] = (count, current_time)

        
        if count > self.max_requests:
            logger.warning(
                f"Too many requests from {client_ip} - Count: {count}"
            )
            return Response("Too many requests", status_code=429)

        
        start_time = time.time()

        
        response = await call_next(request)

        
        process_time = time.time() - start_time

        
        logger.info(
            f"Processed request from {client_ip} in {process_time:.4f} seconds"
        )

        response.headers["X-Process-Time"] = str(process_time)

        return response
