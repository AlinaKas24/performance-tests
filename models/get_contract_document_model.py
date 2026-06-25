from pydantic import BaseModel


class Document(BaseModel):
    url: str
    document: str


class GetContractDocumentResponse(BaseModel):
    tariff: Document
