from pydantic import BaseModel, Field


class MakePurchaseRequest(BaseModel):
    status: str = Field(default="COMPLETED")
    amount: float = Field(default=55.77)
    cardId: str
    accountId: str
    category: str = Field(default="taxi")


class MakePurchaseOperation(BaseModel):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class MakePurchaseOperationResponse(BaseModel):
    operation: MakePurchaseOperation
