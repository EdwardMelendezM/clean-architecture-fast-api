from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional

Base = declarative_base()


class ProductEntity(Base):
    __tablename__ = 'products'
    product_id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    price: float = Column(Float, nullable=True)
    description: Optional[str] = Column(String, nullable=True)
