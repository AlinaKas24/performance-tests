import time

from pydantic import BaseModel, Field

from tools.fakers import fake


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
    email: str = Field(default_factory=fake.email)
    last_name: str = Field(default_factory=fake.last_name)
    first_name: str = Field(default_factory=fake.first_name)
    middle_name: str = Field(default_factory=fake.middle_name)
    phone_number: str = Field(default_factory=fake.phone_number)
