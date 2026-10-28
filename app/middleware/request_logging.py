import logging
import time

from fastapi import Request

logger = logging.getLogger("agtech")


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


async def log_requests(request: Request, call_next):
    start = time.perf_counter()

    response = await call_next(request)

    ms = (time.perf_counter() - start) * 1000

    logger.info(
        "%s %s -> %s (%.0f ms)",
        request.method,
        request.url.path,
        response.status_code,
        ms
    )

    return response