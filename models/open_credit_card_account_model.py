from pydantic import BaseModel

from models.issue_physical_card_model import Card


class OpenCreditCardAccountRequest(BaseModel):
    userId: str


class Account(BaseModel):
    id: str
    type: str
    cards: list[Card]  # Вложенная структура: список карт
    status: str
    balance: float


class OpenCreditCardAccountResponse(BaseModel):
    account: Account
