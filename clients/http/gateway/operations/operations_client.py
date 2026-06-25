from typing import TypedDict
from unicodedata import category

from httpx import Response, QueryParams


from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from models.get_operation_receipt_model import GetOperationReceiptResponse
from models.get_operation_view_model import GetOperationViewResponse
from models.get_operations_model import GetOperationsResponse
from models.get_operations_summary_model import GetOperationsSummaryResponse
from models.make_bill_payment_operation_model import (
    MakeBillPaymentRequest,
    MakeBillPaymentOperationResponse,
)
from models.make_cash_withdrawal_operation_model import (
    MakeCashWithdrawalRequest,
    MakeCashWithdrawalOperationResponse,
)
from models.make_cashback_operation_model import (
    MakeCashbackRequest,
    MakeCashbackOperationResponse,
)
from models.make_fee_operation_model import MakeFeeOperationResponse, MakeFeeRequest
from models.make_purchase_operation_model import (
    MakePurchaseRequest,
    MakePurchaseOperationResponse,
)
from models.make_top_up_operation_model import (
    MakeTopUpRequest,
    MakeTopUpOperationResponse,
)
from models.make_transfer_operation_model import (
    MakeTransferRequest,
    MakeTransferOperationResponse,
)


class GetOperationsQuery(TypedDict):
    account_id: str


class GetOperationReceiptQuery(TypedDict):
    operation_id: str


class OperationsGatewayHTTPClient(HTTPClient):

    def get_operations_api(self, query: GetOperationsQuery) -> Response:
        return self.get("/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsQuery) -> Response:
        return self.get(
            "/v1/operations/operations-summary", params=QueryParams(**query)
        )

    def get_operation_receipt_api(
        self, query: GetOperationReceiptQuery, operation_id: str
    ) -> Response:
        return self.get(
            f"/v1/operations/operation-receipt/{operation_id}",
            params=QueryParams(**query),
        )

    def get_operation_view_api(
        self, query: GetOperationReceiptQuery, operation_id: str
    ) -> Response:
        return self.get(
            f"/api/v1/operations/{operation_id}", params=QueryParams(**query)
        )

    def make_fee_operation_api(self, request: MakeFeeRequest) -> Response:
        return self.post(
            "/api/v1/operations/make-fee-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_top_up_operation_api(self, request: MakeTopUpRequest) -> Response:
        return self.post(
            "/api/v1/operations/make-top-up-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_cashback_operation_api(self, request: MakeCashbackRequest) -> Response:
        return self.post(
            "/api/v1/operations/make-cashback-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_transfer_operation_api(self, request: MakeTransferRequest) -> Response:
        return self.post(
            "/api/v1/operations/make-transfer-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_purchase_operation_api(self, request: MakePurchaseRequest) -> Response:
        return self.post(
            "/api/v1/operations/make-purchase-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_bill_payment_operation_api(
        self, request: MakeBillPaymentRequest
    ) -> Response:
        return self.post(
            "/api/v1/operations/make-bill-payment-operation",
            json=request.model_dump(by_alias=True),
        )

    def make_cash_withdrawal_operation_api(
        self, request: MakeCashWithdrawalRequest
    ) -> Response:
        return self.post(
            "/api/v1/operations/make-cash-withdrawal-operation",
            json=request.model_dump(by_alias=True),
        )

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        query = GetOperationsQuery(account_id=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        query = GetOperationsQuery(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        query = GetOperationReceiptQuery(operation_id=operation_id)
        response = self.get_operation_receipt_api(query, operation_id)
        return response.json()

    def get_operation_view(self, operation_id: str) -> GetOperationViewResponse:
        query = GetOperationReceiptQuery(operation_id=operation_id)
        response = self.get_operation_view_api(query, operation_id)
        return response.json()

    def make_fee_operation(
        self, card_id: str, account_id: str
    ) -> MakeFeeOperationResponse:
        request = MakeFeeRequest(cardId=card_id, accountId=account_id)
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(
        self, card_id: str, account_id: str
    ) -> MakeTopUpOperationResponse:
        request = MakeTopUpRequest(cardId=card_id, accountId=account_id)
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(
        self, card_id: str, account_id: str
    ) -> MakeCashbackOperationResponse:
        request = MakeCashbackRequest(cardId=card_id, accountId=account_id)
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(
        self, card_id: str, account_id: str
    ) -> MakeTransferOperationResponse:
        request = MakeTransferRequest(
            status="COMPLETED", amount=55.77, cardId=card_id, accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(
        self, card_id: str, account_id: str
    ) -> MakePurchaseOperationResponse:
        request = MakePurchaseRequest(
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(
        self, card_id: str, account_id: str
    ) -> MakeBillPaymentOperationResponse:
        request = MakeBillPaymentRequest(cardId=card_id, accountId=account_id)
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(
        self, card_id: str, account_id: str
    ) -> MakeCashWithdrawalOperationResponse:
        request = MakeCashWithdrawalRequest(
            status="COMPLETED", amount=55.77, cardId=card_id, accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
