from pydantic import BaseModel


class EncodeSchema(BaseModel):
    content: str

class EncodeResponse(BaseModel):
    image: str