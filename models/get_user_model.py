from pydantic import BaseModel


class User(BaseModel):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class GetUserResponse(BaseModel):
    user: User
