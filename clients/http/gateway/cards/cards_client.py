from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


# Добавили описание структуры карты
class CardDict(TypedDict):

    id: str
    pin: str
    cvv: str
    type: str
    status: str
    accountId: str
    cardNumber: str
    cardHolder: str
    expiryDate: str
    paymentSystem: str


class IssueVirtualCardRequestDict(TypedDict):

    userId: str
    accountId: str


# Добавили описание структуры ответа выпуска виртуальной карты
class IssueVirtualCardResponseDict(TypedDict):

    card: CardDict


class IssuePhysicalCardRequestDict(TypedDict):
    userId: str
    accountId: str


# Добавили описание структуры ответа выпуска физической карты
class IssuePhysicalCardResponseDict(TypedDict):
    card: CardDict


class CardsGatewayHTTPClient(HTTPClient):
    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> Response:
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(
        self, request: IssuePhysicalCardRequestDict
    ) -> Response:
        return self.post("/api/v1/cards/issue-physical-card", json=request)

    # Добавили новый метод
    def issue_virtual_card(
        self, user_id: str, account_id: str
    ) -> IssueVirtualCardResponseDict:
        request = IssueVirtualCardRequestDict(userId=user_id, accountId=account_id)
        response = self.issue_virtual_card_api(request)
        return response.json()

    # Добавили новый метод
    def issue_physical_card(
        self, user_id: str, account_id: str
    ) -> IssuePhysicalCardResponseDict:
        request = IssuePhysicalCardRequestDict(userId=user_id, accountId=account_id)
        response = self.issue_physical_card_api(request)
        return response.json()


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:

    return CardsGatewayHTTPClient(client=build_gateway_http_client())
