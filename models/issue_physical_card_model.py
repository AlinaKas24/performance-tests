from pydantic import BaseModel


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


class IssuePhysicalCardResponse(BaseModel):
    card: Card


class IssuePhysicalCardRequest(BaseModel):
    user_id: str
    account_id: str
