from pydantic import BaseModel, Field


class MakeTopUpRequest(BaseModel):
    status: str = Field(default="COMPLETED")
    amount: float = Field(default=55.77)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTopUpOperation(BaseModel):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class MakeTopUpOperationResponse(BaseModel):
    operation: MakeTopUpOperation
