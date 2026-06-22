#Создание нового пользователя
import httpx

data={"email": "user133@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"}
response=httpx.post("http://localhost:8003/api/v1/users",json=data)
print(response.json())
user_id = response.json()["user"]["id"]
print(user_id)
data={"userId":user_id}
#Создание депозитного счета
response_deposit=httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account",json=data)
print(response_deposit.text)
account_id = response_deposit.json()["account"]["id"]
print(user_id)
print(account_id)
print(response_deposit.json())
print(response_deposit.status_code)
