import time
from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from models.create_user_model import CreateUserRequest, CreateUserResponse
from models.get_user_model import GetUserResponse


class UsersGatewayHTTPClient(HTTPClient):
    def get_user_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequest) -> Response:
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self) -> CreateUserResponse:
        request = CreateUserRequest()
        response = self.create_user_api(request)
        return response.json()

    def get_user(self, user_id: str) -> GetUserResponse:
        response = self.get_user_api(user_id)
        return response.json()


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    return UsersGatewayHTTPClient(client=build_gateway_http_client())
