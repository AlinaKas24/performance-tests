from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from models.issue_physical_card_model import (
    IssuePhysicalCardRequest,
    IssuePhysicalCardResponse,
)
from models.issue_virtual_card_model import (
    IssueVirtualCardResponse,
    IssueVirtualCardRequest,
)


class CardsGatewayHTTPClient(HTTPClient):
    def issue_virtual_card_api(self, request: IssueVirtualCardRequest) -> Response:
        return self.post(
            "/api/v1/cards/issue-virtual-card", json=request.model_dump(by_alias=True)
        )

    def issue_physical_card_api(self, request: IssuePhysicalCardRequest) -> Response:
        return self.post(
            "/api/v1/cards/issue-physical-card", json=request.model_dump(by_alias=True)
        )

    def issue_virtual_card(
        self, user_id: str, account_id: str
    ) -> IssueVirtualCardResponse:
        request = IssueVirtualCardRequest(userId=user_id, accountId=account_id)
        response = self.issue_virtual_card_api(request)
        return response.json()

    def issue_physical_card(
        self, user_id: str, account_id: str
    ) -> IssuePhysicalCardResponse:
        request = IssuePhysicalCardRequest(user_id=user_id, account_id=account_id)
        response = self.issue_physical_card_api(request)
        return response.json()


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:

    return CardsGatewayHTTPClient(client=build_gateway_http_client())
