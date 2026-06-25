from typing import List

from pydantic import BaseModel


class OperationsResponse(BaseModel):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class GetOperationsResponse(BaseModel):
    operations: List[OperationsResponse]
