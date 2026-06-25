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
    last_name: str = Field(default="string")
    first_name: str = Field(default="string")
    middle_name: str = Field(default="string")
    phone_number: str = Field(default="string")
