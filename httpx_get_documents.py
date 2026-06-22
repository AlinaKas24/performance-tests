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
print(account_id)
response_get_documents=httpx.get(f"http://localhost:8003/api/v1/documents/tariff-document/{account_id}")
print(response_get_documents.text)
print(response_get_documents.status_code)
response_get_contract=httpx.get(f"http://localhost:8003/api/v1/documents/contract-document/{account_id}")
print(response_get_contract.text)
print(response_get_contract.status_code)