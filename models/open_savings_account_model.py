from pydantic import BaseModel

from models.issue_physical_card_model import Card


class Account(BaseModel):
    id: str
    type: str
    cards: list[Card]  # Вложенная структура: список карт
    status: str
    balance: float


class OpenSavingsAccountResponse(BaseModel):
    account: Account


class OpenSavingsAccountRequest(BaseModel):
    user_id: str
