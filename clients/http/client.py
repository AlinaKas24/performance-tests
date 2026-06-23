from typing import Any

from httpx import Client, URL, QueryParams, Response
from httpx._types import RequestFiles


class HTTPClient:
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        return self.client.get(url, params=params)

    def post(
        self,
        url: URL | str,
        params: QueryParams | None = None,
        json: Any | None = None,
        files: RequestFiles | None = None,
    ) -> Response:
        return self.client.post(url, params=params, json=json, files=files)
