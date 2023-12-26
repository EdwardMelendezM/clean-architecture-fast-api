from typing import Optional, List
from decimal import Decimal
from pydantic import BaseModel


class Product:
    def __init__(self, product_id: int, name: str, price: Decimal, description: Optional[str] = None):
        """
        Representa un producto.

        :param product_id: Identificador único del producto.
        :param name: Nombre del producto.
        :param price: Precio del producto (utilizando Decimal para representar valores monetarios).
        :param description: Descripción opcional del producto.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description


class CreateBodyProduct:
    def __init__(self, name: str, price: Decimal, description: Optional[str] = None):
        """
        Representa los datos necesarios para crear un nuevo producto.

        :param name: Nombre del producto.
        :param price: Precio del producto (utilizando Decimal para representar valores monetarios).
        :param description: Descripción opcional del producto.
        """
        self.name = name
        self.price = price
        self.description = description


class UpdateBodyProduct:
    def __init__(self, name: Optional[str] = None, price: Optional[Decimal] = None, description: Optional[str] = None):
        """
        Representa los datos opcionales para actualizar un producto.

        :param name: Nuevo nombre del producto.
        :param price: Nuevo precio del producto (utilizando Decimal para representar valores monetarios).
        :param description: Nueva descripción del producto.
        """
        self.name = name
        self.price = price
        self.description = description


class PaginatedProductList(BaseModel):
    items: List[Product]
    total_items: int
