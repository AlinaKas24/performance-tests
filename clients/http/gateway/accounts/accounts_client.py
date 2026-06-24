from typing import TypedDict

from httpx import Response, Client, QueryParams

from clients.http.client import HTTPClient


class GetAccountsQuery(TypedDict):
    userId: str


class OpenAccountRequest(TypedDict):
    userId: str


class AccountsGatewayHTTPClient(HTTPClient):
    def get_accounts_api(self, query: GetAccountsQuery) -> Response:
        return self.get(f"/api/v1/accounts", params=QueryParams(**query))

    def open_deposit_account_api(self, request: OpenAccountRequest) -> Response:
        return self.post(f"/api/v1/accounts/open-deposit-account", json=request)

    def open_savings_account_api(self, request: OpenAccountRequest) -> Response:
        return self.post(f"/api/v1/accounts/open-savings-account", json=request)

    def open_debit_card_account_api(self, request: OpenAccountRequest) -> Response:
        return self.post(f"/api/v1/accounts/open-debit-card-account", json=request)

    def open_credit_card_account_api(self, request: OpenAccountRequest) -> Response:
        return self.post(f"/api/v1/accounts/open-credit_card-account", json=request)


account_clent = AccountsGatewayHTTPClient(
    client=Client(base_url="https://localhost:8003")
)
