from pydantic import BaseModel


class OperationViewResponse(BaseModel):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class GetOperationViewResponse(BaseModel):
    operation: OperationViewResponse
