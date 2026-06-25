from pydantic import BaseModel


class OperationsSummaryResponse(BaseModel):
    spent_amount: int
    received_amount: int
    cashback_amount: int


class GetOperationsSummaryResponse(BaseModel):
    summary: OperationsSummaryResponse
