import time

from pydantic import BaseModel, Field


class User(BaseModel):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class CreateUserResponse(BaseModel):
    user: User


class CreateUserRequest(BaseModel):
    email: str = Field(default=f"user.{time.time()}@example.com")
    lastName: str = Field(default="string")
    firstName: str = Field(default="string")
    middleName: str = Field(default="string")
    phoneNumber: str = Field(default="string")
