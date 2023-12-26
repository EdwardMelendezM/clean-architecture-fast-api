from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional

Base = declarative_base()


class ProductEntity(Base):
    """
    Clase que representa la entidad Product en la base de datos.

    Attributes:
    - product_id: Identificador único del producto (clave primaria).
    - name: Nombre del producto.
    - price: Precio del producto.
    - description: Descripción opcional del producto.
    """

    __tablename__ = 'products'
    product_id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    price: int = Column(Integer, nullable=False)
    description: Optional[str] = Column(String, nullable=True)
