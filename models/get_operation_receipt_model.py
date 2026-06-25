from pydantic import BaseModel


class OperationReceiptResponse(BaseModel):
    url: str
    document: str


class GetOperationReceiptResponse(BaseModel):
    receipt: OperationReceiptResponse
