from pydantic import BaseModel


class OperationsSummaryResponse(BaseModel):
    spentAmount: int
    receivedAmount: int
    cashbackAmount: int


class GetOperationsSummaryResponse(BaseModel):
    summary: OperationsSummaryResponse
