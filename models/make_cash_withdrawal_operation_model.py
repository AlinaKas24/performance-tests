from pydantic import BaseModel, Field


class MakeCashWithdrawalOperation(BaseModel):
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class MakeCashWithdrawalOperationResponse(BaseModel):
    operation: MakeCashWithdrawalOperation


class MakeCashWithdrawalRequest(BaseModel):
    status: str = Field(default="COMPLETED")
    amount: float = Field(default=55.77)
    cardId: str
    accountId: str
    category: str = Field(default="taxi")
