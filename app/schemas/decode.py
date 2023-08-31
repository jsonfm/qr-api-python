from typing import List, Optional
from pydantic import BaseModel


class DecodeSchema(BaseModel):
    image: str


class Rect(BaseModel):
    left: int
    top: int
    width: int
    height: int

class Point(BaseModel):
    x: int
    y: int

class DecodeResponse(BaseModel):
    content: str
    type: Optional[str]
    rect: Optional[Rect]
    quality: Optional[int]
    polygon: Optional[List[Point]]
    orientation: Optional[str]