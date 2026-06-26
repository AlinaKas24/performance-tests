from enum import StrEnum

from pydantic import BaseModel, Field

from tools.fakers import fake


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class MakeCashWithdrawalOperation(BaseModel):
    id: str
    type: str
    status: str
    amount: int
    card_id: str
    category: str
    created_at: str
    account_id: str


class MakeCashWithdrawalOperationResponse(BaseModel):
    operation: MakeCashWithdrawalOperation


class MakeCashWithdrawalRequest(BaseModel):
    status: OperationStatus
    amount: float = Field(default_factory=fake.amount)
    card_id: str
    account_id: str
    category: str = Field(default="taxi")
