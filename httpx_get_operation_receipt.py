#Создание нового пользователя
import httpx


# data={"email": "user133@example.com",
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string",
#   "phoneNumber": "string"}
# response=httpx.post("http://localhost:8003/api/v1/users",json=data)
# print(response.json())
# user_id = response.json()["user"]["id"]
# print(user_id)
#data={"userId":user_id}
data={"userId":"8962a342-d225-45d7-a287-8ae345a4f459"}
response_open_account=httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account",json=data)
account_id = response_open_account.json()["account"]["id"]
card_id=response_open_account.json()["account"]["cards"][0]["id"]
print(account_id)
print(card_id)
data={  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": card_id,
  "accountId":account_id,
  "category": "taxi"}
response_operation=httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation",json=data)
operation_id=response_operation.json()["operation"]["id"]
response_get_receipt=httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}")
print(response_get_receipt.json())
print(response_get_receipt.status_code)
