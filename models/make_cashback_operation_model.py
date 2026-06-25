from pydantic import BaseModel, Field


class MakeCashbackOperation(BaseModel):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class MakeCashbackOperationResponse(BaseModel):
    operation: MakeCashbackOperation


class MakeCashbackRequest(BaseModel):
    status: str = Field(default="COMPLETED")
    amount: float = Field(default=55.77)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
