from pydantic import BaseModel


class User(BaseModel):
    id: str
    email: str
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class GetUserResponse(BaseModel):
    user: User
