# #Создание нового пользователя
# import httpx
# import time

# data={"email": f"user.{time.time()}@example.com",
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string",
#   "phoneNumber": "string"}
# response=httpx.post("http://localhost:8003/api/v1/users",json=data)
# print(response.json())
# user_id = response.json()["user"]["id"]
# print(user_id)
# data={"userId":user_id}

import httpx
import time

client = httpx.Client(
    base_url="http://localhost:8003/api/",
    timeout=5,
    headers={"Autarization": "Bearer ..."},
)
data = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string",
}

response = client.post("v1/users", json=data)
print(response.text)
print(response.request.headers)
