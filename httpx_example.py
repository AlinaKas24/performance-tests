import httpx

# response=httpx.get("https://jsonplaceholder.typicode.com/todos/1")
# print(response.json(),response.status_code)
#
# data={
#     "title":"new task",
#     "completed":False,
#     "user_id":1}
# response=httpx.post("https://jsonplaceholder.typicode.com/todos",data=data)
#
# print(response.json(),response.status_code)
#
# headers={"Authorization":"Bearer my_secret_token"}
# response=httpx.get("https://httpbin.org/get",headers=headers)
# print(response.text,response.status_code)
params={"userId":1}
response=httpx.get("https://jsonplaceholder.typicode.com/todos",params=params)
print(response.request.url)
print(response.request.headers)
print( response.request.url.query)