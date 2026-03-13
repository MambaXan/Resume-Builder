from pydantic import BaseModel, EmailStr
from typing import List, Optional

class ResumeBase(BaseModel):
    title: str

class ResumeCreate(ResumeBase):
    pass

class Resume(ResumeBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True



class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    resumes: List[Resume] = []

    class Config:
        from_attributes = True