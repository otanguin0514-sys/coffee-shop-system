from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from decimal import Decimal


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    role: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    category_id: int
    available: bool = True
    stock_quantity: int = 0


class ProductOut(ProductBase):
    id: int


class ReviewCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    title: Optional[str] = None
    comment: str
    product_id: Optional[int] = None
    shop_id: int = 1


class ReviewOut(BaseModel):
    id: int
    user_id: int
    shop_id: int
    product_id: Optional[int]
    rating: int
    title: Optional[str]
    comment: str
    created_at: str


class OrderItemInput(BaseModel):
    product_id: int
    quantity: int = 1


class OrderCreate(BaseModel):
    items: List[OrderItemInput]
    payment_method: str = "card"
    notes: Optional[str] = None


class InventoryOut(BaseModel):
    id: int
    product_id: int
    stock_level: int
    reorder_level: int
    unit: str
