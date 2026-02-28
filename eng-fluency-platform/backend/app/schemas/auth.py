from typing import Optional
from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: Optional[str] = None
    tenant_id: Optional[str] = None

class Login(BaseModel):
    email: EmailStr
    password: str

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    full_name: Optional[str] = None
    role: Optional[str] = "student"

class UserCreate(UserBase):
    email: EmailStr
    password: str

class User(UserBase):
    id: str
    tenant_id: str

    class Config:
        from_attributes = True
