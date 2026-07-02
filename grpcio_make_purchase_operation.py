import grpc

from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import (
    AccountsGatewayServiceStub,
)
from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import (
    OpenCreditCardAccountRequest,
)

from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import (
    OperationsGatewayServiceStub,
)
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationRequest,
)
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import (
    UsersGatewayServiceStub,
)
from contracts.services.operations.operation_pb2 import OperationStatus
from tools.fakers import fake

channel = grpc.insecure_channel("localhost:9003")

users_gateway_service = UsersGatewayServiceStub(channel)
accounts_gateway_service = AccountsGatewayServiceStub(channel)
operations_gateway_service = OperationsGatewayServiceStub(channel)

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

open_credit_card_account_request = OpenCreditCardAccountRequest(user_id=user_id)
open_credit_card_account_response = accounts_gateway_service.OpenCreditCardAccount(
    open_credit_card_account_request
)
account_id = open_credit_card_account_response.account.id
card_id = open_credit_card_account_response.account.cards[0].id
print("Open credit card account response: ", open_credit_card_account_response)
print("Account id: ", account_id)
print("Card id: ", account_id)

make_purchase_operation_request = MakePurchaseOperationRequest(
    status=OperationStatus.OPERATION_STATUS_IN_PROGRESS,
    amount=fake.amount(),
    card_id=card_id,
    category=fake.category(),
    account_id=account_id,
)
make_purchase_operation_response = operations_gateway_service.MakePurchaseOperation(
    make_purchase_operation_request
)
print("Make purchase operation response:", make_purchase_operation_response)
