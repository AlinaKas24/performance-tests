from pydantic import BaseModel, Field


class MakeTransferOperation(BaseModel):
    id: str
    type: str
    status: str
    amount: int
    card_id: str
    category: str
    created_at: str
    account_id: str


class MakeTransferOperationResponse(BaseModel):
    operation: MakeTransferOperation


class MakeTransferRequest(BaseModel):
    status: str = Field(default="COMPLETED")
    amount: float = Field(default=55.77)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
