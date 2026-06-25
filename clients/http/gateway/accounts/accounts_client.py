from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from models.get_accounts_model import GetAccountsResponse
from models.open_credit_card_account_model import (
    OpenCreditCardAccountRequest,
    OpenCreditCardAccountResponse,
)
from models.open_debit_card_account_model import (
    OpenDebitCardAccountResponse,
    OpenDebitCardAccountRequest,
)
from models.open_deposit_account_model import (
    OpenDepositAccountRequest,
    OpenDepositAccountResponse,
)
from models.open_savings_account_model import (
    OpenSavingsAccountResponse,
    OpenSavingsAccountRequest,
)


class GetAccountsQueryDict(TypedDict):
    userId: str


class AccountsGatewayHTTPClient(HTTPClient):

    def get_accounts_api(self, query: GetAccountsQueryDict):

        return self.get("/api/v1/accounts", params=QueryParams(**query))

    def open_deposit_account_api(self, request: OpenDepositAccountRequest) -> Response:

        return self.post(
            "/api/v1/accounts/open-deposit-account", json=request.model_dump()
        )

    def open_savings_account_api(self, request: OpenSavingsAccountRequest) -> Response:

        return self.post(
            "/api/v1/accounts/open-savings-account", json=request.model_dump()
        )

    def open_debit_card_account_api(
        self, request: OpenDebitCardAccountRequest
    ) -> Response:

        return self.post(
            "/api/v1/accounts/open-debit-card-account", json=request.model_dump()
        )

    def open_credit_card_account_api(
        self, request: OpenCreditCardAccountRequest
    ) -> Response:

        return self.post(
            "/api/v1/accounts/open-credit-card-account", json=request.model_dump()
        )

    # Добавили новый метод
    def get_accounts(self, user_id: str) -> GetAccountsResponse:
        query = GetAccountsQueryDict(userId=user_id)
        response = self.get_accounts_api(query)
        return response.json()

    # Добавили новый метод
    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponse:
        request = OpenDepositAccountRequest(userId=user_id)
        response = self.open_deposit_account_api(request)
        return response.json()

    # Добавили новый метод
    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponse:
        request = OpenSavingsAccountRequest(userId=user_id)
        response = self.open_savings_account_api(request)
        return response.json()

    # Добавили новый метод
    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponse:
        request = OpenDebitCardAccountRequest(userId=user_id)
        response = self.open_debit_card_account_api(request)
        return response.json()

    # Добавили новый метод
    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponse:
        request = OpenCreditCardAccountRequest(userId=user_id)
        response = self.open_credit_card_account_api(request)
        return response.json()


def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())
