from pydantic import BaseModel


class OperationViewResponse(BaseModel):
    id: str
    type: str
    status: str
    amount: int
    card_id: str
    category: str
    created_at: str
    account_id: str


class GetOperationViewResponse(BaseModel):
    operation: OperationViewResponse
