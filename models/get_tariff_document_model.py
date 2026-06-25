from pydantic import BaseModel


class Document(BaseModel):
    url: str
    document: str


class GetTariffDocumentResponse(BaseModel):
    tariff: Document
