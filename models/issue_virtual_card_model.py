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
    account_id: str
    card_number: str
    card_holder: str
    expiry_date: str
    payment_system: str


class IssueVirtualCardResponse(BaseModel):

    card: Card
