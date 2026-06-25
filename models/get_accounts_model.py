from typing import List

from pydantic import BaseModel

from models.issue_physical_card_model import Card


class Account(BaseModel):
    id: str
    type: str
    cards: list[Card]
    status: str
    balance: float


class GetAccountsResponse(BaseModel):

    accounts: List[Account]
