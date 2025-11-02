# base_client.py
import httpx
import time
from browserforge.headers import HeaderGenerator
from urllib.parse import urljoin

from logger.logger import get_logger

logger = get_logger("BaseClient")

class BaseClient:
    def __init__(self, base_url: str, retries: int = 5, timeout: int = 10, backoff: float = 1.5):
        self.base_url = base_url.rstrip("/")
        self.retries = retries
        self.timeout = timeout
        self.backoff = backoff

    def _request(self, method: str, endpoint: str, **kwargs) -> dict:
        url = urljoin(self.base_url, endpoint)

        # Build browser-like headers using HeaderGenerator and merge them with
        # any headers passed in via kwargs. We MUST NOT overwrite user-provided
        # headers; user headers (param_headers) take precedence.
        hg = HeaderGenerator(device='desktop', locale='en-US', http_version=2)
        try:
            # The config elsewhere uses headerGenerator.generate(), so prefer
            # to call generate() if available.
            custom_headers = hg.generate() if hasattr(hg, "generate") else getattr(hg, "headers", {})
        except Exception as e:
            logger.warning(f"Failed to generate headers from HeaderGenerator: {e}")
            custom_headers = {}

        # Headers passed by the caller (if any)
        param_headers = kwargs.get('headers', None)

        # If caller provided headers and they're a dict, merge so that caller's
        # headers override generated defaults. If caller provided non-dict
        # headers, keep them unchanged and log a warning.
        if param_headers:
            if isinstance(param_headers, dict):
                merged_headers = {**custom_headers, **param_headers}
            else:
                logger.warning("Request headers passed are not a dict; keeping them unchanged.")
                merged_headers = param_headers
        else:
            merged_headers = custom_headers

        # Put the merged headers back into kwargs for the request
        kwargs['headers'] = merged_headers

        for attempt in range(1, self.retries + 1):
            try:
                logger.debug(f"[Attempt {attempt}] {method} {url} | Params: {kwargs.get('params')} | Data: {kwargs.get('json')}")
                response = httpx.request(method, url, timeout=self.timeout, **kwargs)
                response.raise_for_status()
                logger.debug(f"[Success] {method} {url} | Status: {response.status_code}")
                return {
                    "status": response.status_code,
                    "headers": dict(response.headers),
                    "cookies": dict(response.cookies),
                    "body": response.text
                }
            except httpx.RequestError as e:
                logger.warning(f"[Retry {attempt}/{self.retries}] Error calling {url}: {e}")
                if attempt == self.retries:
                    logger.error(f"[Failed] All retries exhausted for {url}")
                    raise
                sleep_time = self.backoff ** attempt
                logger.debug(f"Sleeping for {sleep_time:.2f}s before retry")
                time.sleep(sleep_time)
        
        return {}
