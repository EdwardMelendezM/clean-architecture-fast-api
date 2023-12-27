from abc import ABC, abstractmethod
from typing import List, Optional

from domain.products_entities import Product, CreateBodyProduct, UpdateBodyProduct


class ProductsRepository(ABC):
    @abstractmethod
    def get_products(self) -> List[Product]:
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        pass

    @abstractmethod
    def create_product(self, product: CreateBodyProduct) -> Product:
        pass

    @abstractmethod
    def update_product(self, product_id: int, update_body: UpdateBodyProduct) -> Optional[Product]:
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> None:
        pass
