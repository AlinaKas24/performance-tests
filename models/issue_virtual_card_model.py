from pydantic import BaseModel


class IssueVirtualCardRequest(BaseModel):

    userId: str
    accountId: str


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


class IssueVirtualCardResponse(BaseModel):

    card: Card
