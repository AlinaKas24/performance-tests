from typing import TypedDict

from httpx import Response, QueryParams, Client
from redis.commands.search.field import Field

from clients.http.client import HTTPClient


class GetOperationsQuery(TypedDict):
    accountrId: str


class GetOperationReceiptQuery(TypedDict):
    operation_id: str


class MakeFeeRequest(TypedDict):
    status: str
    amount: int
    cardId: str
    accountId: str


class MakePurchaseRequest(TypedDict):
    status: str
    amount: int
    cardId: str
    accountId: str
    category: str


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
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeFeeRequest) -> Response:
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeFeeRequest) -> Response:
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeFeeRequest) -> Response:
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseRequest) -> Response:
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeFeeRequest) -> Response:
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeFeeRequest) -> Response:
        return self.post(
            "/api/v1/operations/make-cash-withdrawal-operation", json=request
        )


operations_clent = OperationsGatewayHTTPClient(
    client=Client(base_url="https://localhost:8003")
)
