from pydantic import BaseModel, Field, EmailStr, HttpUrl
from datetime import datetime

class Contact(BaseModel):
    id: int
    name: str = Field(...,min_length=2, max_length=200)
    email: EmailStr
    url: HttpUrl| None = Field(default=None)
    gender: int = Field(..., strict=True, ge=0, le=2)
    message: str = Field(..., max_length=200)
    is_enable: bool = Field(default=False)
    created_at: datetime
