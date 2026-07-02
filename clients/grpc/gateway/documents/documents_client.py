from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import (
    DocumentsGatewayServiceStub,
)
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import (
    GetContractDocumentRequest,
    GetContractDocumentResponse,
)
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import (
    GetTariffDocumentRequest,
    GetTariffDocumentResponse,
)


class DocumentsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с DocumentGatewayService.
    Предоставляет высокоуровневые методы для получения документов.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к UsersGatewayService.
        """
        super().__init__(channel)

        self.stub = DocumentsGatewayServiceStub(
            channel
        )  # gRPC-стаб, сгенерированный из .proto

    def get_tariff_document_api(
        self, request: GetTariffDocumentRequest
    ) -> GetTariffDocumentResponse:
        """
        Низкоуровневый вызов метода GetTariffDocument через gRPC.

        :param request: gRPC-запрос с ID аккаунтом пользователя.
        :return: Ответ от сервиса с данными пользователя.
        """
        return self.stub.GetTariffDocument(request)

    def get_contract_document_api(
        self, request: GetContractDocumentRequest
    ) -> GetContractDocumentResponse:
        """
        Низкоуровневый вызов метода GetContractDocument через gRPC.

        :param request: gRPC-запрос с ID аккаунтом пользователя.
        :return: Ответ от сервиса с данными пользователя.
        """
        return self.stub.GetContractDocument(request)

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponse:
        """
        Получение данных пользователя по его ID.

        :param account_id: Идентификатор аккаунта пользователя.
        :return: Ответ с информацией о пользователе.
        """
        request = GetTariffDocumentRequest(account_id=account_id)
        return self.get_tariff_document_api(request)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponse:
        """
        Получение данных пользователя по его ID.

        :param account_id: Идентификатор аккаунта пользователя.
        :return: Ответ с информацией о пользователе.
        """
        request = GetContractDocumentRequest(account_id=account_id)
        return self.get_contract_document_api(request)


def build_documents_gateway_grpc_client() -> DocumentsGatewayGRPCClient:
    return DocumentsGatewayGRPCClient(channel=build_gateway_grpc_client())
