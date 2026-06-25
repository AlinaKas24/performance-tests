from typing import TypedDict

from httpx import Response, Client

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class DocumentDict(TypedDict):
    url: str
    document: str


class GetTariffDocumentResponseDict(TypedDict):
    tariff: DocumentDict


class GetTContractDocumentResponseDict(TypedDict):
    tariff: DocumentDict


class DocumentsGatewayHTTPClient(HTTPClient):
    def get_tariff_document_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        response = self.get_tariff_document_api(account_id)
        return response.json()

    def get_contract_document(
        self, account_id: str
    ) -> GetTContractDocumentResponseDict:
        response = self.get_contract_document_api(account_id)
        return response.json()


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())
