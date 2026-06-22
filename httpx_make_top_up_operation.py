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
response_open_account=httpx.post("http://localhost:8003/api/v1/accounts/open-debit-card-account",json=data)
account_id = response_open_account.json()["account"]["id"]
card_id=response_open_account.json()["account"]["cards"][0]["id"]
print(card_id)
data={
  "status": "COMPLETED",
  "amount": 10,
  "cardId": card_id,
  "accountId": account_id
}
response_make_top_up_operation=httpx.post("http://localhost:8003/api/v1/operations/make-top-up-operation",json=data)

print(response_make_top_up_operation.text)
print(response_make_top_up_operation.status_code)

response_get_account=httpx.get("http://localhost:8003/api/v1/accounts",params={"userId": "8962a342-d225-45d7-a287-8ae345a4f459"})

print(response_get_account.text)
print(response_get_account.status_code)