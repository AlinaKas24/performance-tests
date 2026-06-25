from typing import TypedDict
from unicodedata import category

from httpx import Response, QueryParams


from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class GetOperationsQuery(TypedDict):
    account_id: str


class GetOperationReceiptQuery(TypedDict):
    operation_id: str


class MakeFeeRequest(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseRequest(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str


class OperationsResponseDict(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class GetOperationsResponseDict(TypedDict):
    operations: list[OperationsResponseDict]


class OperationsSummaryResponseDict(TypedDict):
    spentAmount: int
    receivedAmount: int
    cashbackAmount: int


class GetOperationsSummaryResponseDict(TypedDict):
    summary: OperationsSummaryResponseDict


class OperationReceiptResponseDict(TypedDict):
    url: str
    document: str


class GetOperationReceiptResponseDict(TypedDict):
    receipt: OperationReceiptResponseDict


class OperationViewResponseDict(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class GetOperationViewResponseDict(TypedDict):
    operation: OperationViewResponseDict


class MakeFeeOperationResponse(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class MakeFeeOperationResponseDict(TypedDict):
    operation: MakeFeeOperationResponse


class MakeTopUpOperationResponse(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class MakeTopUpOperationResponseDict(TypedDict):
    operation: MakeTopUpOperationResponse


class MakeCashbackOperationResponse(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class MakeCashbackOperationResponseDict(TypedDict):
    operation: MakeCashbackOperationResponse


class MakeTransferOperationResponse(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class MakeTransferOperationResponseDict(TypedDict):
    operation: MakeTransferOperationResponse


class MakePurchaseOperationResponse(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class MakePurchaseOperationResponseDict(TypedDict):
    operation: MakePurchaseOperationResponse


class MakeBillPaymentOperationResponse(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class MakeBillPaymentOperationResponseDict(TypedDict):
    operation: MakeBillPaymentOperationResponse


class MakeCashWithdrawalOperationResponse(TypedDict):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    operation: MakeCashWithdrawalOperationResponse


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

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQuery(account_id=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(
        self, account_id: str
    ) -> GetOperationsSummaryResponseDict:
        query = GetOperationsQuery(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def get_operation_receipt(
        self, operation_id: str
    ) -> GetOperationReceiptResponseDict:
        query = GetOperationReceiptQuery(operation_id=operation_id)
        response = self.get_operation_receipt_api(query, operation_id)
        return response.json()

    def get_operation_view(self, operation_id: str) -> GetOperationViewResponseDict:
        query = GetOperationReceiptQuery(operation_id=operation_id)
        response = self.get_operation_view_api(query, operation_id)
        return response.json()

    def make_fee_operation(
        self, card_id: str, account_id: str
    ) -> MakeFeeOperationResponseDict:
        request = MakeFeeRequest(
            status="COMPLETED", amount=55.77, cardId=card_id, accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(
        self, card_id: str, account_id: str
    ) -> MakeTopUpOperationResponseDict:
        request = MakeFeeRequest(
            status="COMPLETED", amount=55.77, cardId=card_id, accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(
        self, card_id: str, account_id: str
    ) -> MakeCashbackOperationResponseDict:
        request = MakeFeeRequest(
            status="COMPLETED", amount=55.77, cardId=card_id, accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(
        self, card_id: str, account_id: str
    ) -> MakeTransferOperationResponseDict:
        request = MakeFeeRequest(
            status="COMPLETED", amount=55.77, cardId=card_id, accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(
        self, card_id: str, account_id: str
    ) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseRequest(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category="taxi",
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(
        self, card_id: str, account_id: str
    ) -> MakeBillPaymentOperationResponseDict:
        request = MakeFeeRequest(
            status="COMPLETED", amount=55.77, cardId=card_id, accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(
        self, card_id: str, account_id: str
    ) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeFeeRequest(
            status="COMPLETED", amount=55.77, cardId=card_id, accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
