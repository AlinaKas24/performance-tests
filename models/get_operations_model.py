from typing import List

from pydantic import BaseModel


class OperationsResponse(BaseModel):
    id: str
    type: str
    status: str
    amount: int
    card_id: str
    category: str
    created_at: str
    account_id: str


class GetOperationsResponse(BaseModel):
    operations: List[OperationsResponse]
