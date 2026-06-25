import time
from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class UserDict(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class GetUserResponseDict(TypedDict):
    user: UserDict


class CreateUserRequestDict(TypedDict):
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class CreateUserResponseDict(TypedDict):
    user: UserDict


class UsersGatewayHTTPClient(HTTPClient):
    def get_user_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        return self.post("/api/v1/users", json=request)

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id)
        return response.json()

    def create_user(self) -> CreateUserResponseDict:
        request = CreateUserRequestDict(
            email=f"user.{time.time()}@example.com",
            lastName="string",
            firstName="string",
            middleName="string",
            phoneNumber="string",
        )
        response = self.create_user_api(request)
        return response.json()


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    return UsersGatewayHTTPClient(client=build_gateway_http_client())
