from typing import Literal
from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    mobile: str = Field(pattern=r"^[6-9]\d{9}$")
    password: str = Field(min_length=8, max_length=64)
    role: Literal["farmer", "buyer"]