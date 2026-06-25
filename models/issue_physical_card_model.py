from pydantic import BaseModel


class Card(BaseModel):

    id: str
    pin: str
    cvv: str
    type: str
    status: str
    accountId: str
    cardNumber: str
    cardHolder: str
    expiryDate: str
    paymentSystem: str


class IssuePhysicalCardResponse(BaseModel):
    card: Card


class IssuePhysicalCardRequest(BaseModel):
    userId: str
    accountId: str
