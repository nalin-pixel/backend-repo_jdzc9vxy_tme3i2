"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user"
- Product -> "product"
- ContactSubmission -> "contactsubmission"
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

class ContactSubmission(BaseModel):
    """Contact form submissions (collection name: contactsubmission)"""
    name: str = Field(..., min_length=1)
    email: EmailStr
    phone: Optional[str] = None
    service: Optional[str] = Field(None, description="Service interested in")
    message: str = Field(..., min_length=1)
