from typing import Any, TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class CreateUserRequest(TypedDict):
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class UsersGatewayHTTPClient(HTTPClient):
    def get_user_api(self, user_id: str) -> Response:
        return self.get(f"/v1/users/{user_id}")

    def post_user_api(self, request) -> Response:
        return self.post("/v1/users", json=request)
