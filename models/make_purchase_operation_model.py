from pydantic import BaseModel, Field


class MakePurchaseRequest(BaseModel):
    status: str = Field(default="COMPLETED")
    amount: float = Field(default=55.77)
    card_id: str
    account_id: str
    category: str = Field(default="taxi")


class MakePurchaseOperation(BaseModel):
    id: str
    type: str
    status: str
    amount: int
    card_id: str
    category: str
    created_at: str
    account_id: str


class MakePurchaseOperationResponse(BaseModel):
    operation: MakePurchaseOperation
