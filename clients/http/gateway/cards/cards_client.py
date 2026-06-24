from typing import TypedDict

from httpx import Response, Client

from clients.http.client import HTTPClient


class CreateVirtualCardRequest(TypedDict):
    userId: str
    accountId: str


class CreatePhysicalCardRequest(TypedDict):
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):

    def issue_virtual_card_api(self, request: CreateVirtualCardRequest) -> Response:
        return self.post(f"/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: CreatePhysicalCardRequest) -> Response:
        return self.post("/api/v1/cards/issue-physical-card", json=request)


card_clent = CardsGatewayHTTPClient(client=Client(base_url="https://localhost:8003"))
