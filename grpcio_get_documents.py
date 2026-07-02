import grpc

from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import (
    AccountsGatewayServiceStub,
)
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import (
    OpenSavingsAccountRequest,
)
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import (
    DocumentsGatewayServiceStub,
)
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import (
    GetContractDocumentRequest,
)
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import (
    GetTariffDocumentRequest,
)
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import (
    UsersGatewayServiceStub,
)
from tools.fakers import fake

channel = grpc.insecure_channel("localhost:9003")
users_gateway_service = UsersGatewayServiceStub(channel)
accounts_gateway_service = AccountsGatewayServiceStub(channel)
documents_gateway_service = DocumentsGatewayServiceStub(channel)

create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number(),
)
create_user_response = users_gateway_service.CreateUser(create_user_request)
user_id = create_user_response.user.id
print("Create user response: ", create_user_response)
print("User id: ", user_id)

open_savings_account_request = OpenSavingsAccountRequest(user_id=user_id)
open_savings_account_response = accounts_gateway_service.OpenSavingsAccount(
    open_savings_account_request
)
account_id = open_savings_account_response.account.id

print("Open savings account response: ", open_savings_account_response)
print("Account id: ", account_id)

get_tariff_document_request = GetTariffDocumentRequest(account_id=account_id)
get_tariff_document_response = documents_gateway_service.GetTariffDocument(
    get_tariff_document_request
)
print("Get tariff document response:", get_tariff_document_response)

get_contract_document_request = GetContractDocumentRequest(account_id=account_id)
get_contract_document_response = documents_gateway_service.GetContractDocument(
    get_contract_document_request
)
print("Get contract document response:", get_contract_document_response)
