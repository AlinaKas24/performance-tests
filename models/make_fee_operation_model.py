from pydantic import BaseModel, Field


class MakeFeeRequest(BaseModel):
    status: str = Field(default="COMPLETED")
    amount: float = Field(default=55.77)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperation(BaseModel):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class MakeFeeOperationResponse(BaseModel):
    operation: MakeFeeOperation
