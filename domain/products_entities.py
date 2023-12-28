from typing import Optional, List
from pydantic import BaseModel


class Product(BaseModel):
    product_id: int
    name: str
    price: Optional[float] = None
    description: Optional[str] = None


class CreateBodyProduct(BaseModel):
    name: str
    price: Optional[float] = None
    description: Optional[str] = None


class UpdateBodyProduct(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None


class PaginatedProductList(BaseModel):
    items: List[Product]
    total_items: int
