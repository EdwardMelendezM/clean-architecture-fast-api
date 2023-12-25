# En el archivo domain/products_usecase.py

from abc import ABC, abstractmethod
from typing import List

from domain.products_entities import Product, CreateBodyProduct, UpdateBodyProduct
from domain.products_repository import ProductsRepository
from domain.products_usecase import ProductsUseCase


class DefaultProductsUseCase(ProductsUseCase):
    def __init__(self, repository: ProductsRepository):
        self.repository = repository

    def get_products(self) -> List[Product]:
        return self.repository.get_products()

    def get_product_by_id(self, product_id: int) -> Product:
        return self.repository.get_product_by_id(product_id)

    def create_product(self, product_body: CreateBodyProduct) -> Product:
        return self.repository.create_product(product_body)

    def update_product(self, product_id: int, update_body: UpdateBodyProduct) -> Product:
        return self.repository.update_product(product_id, update_body)

    def delete_product(self, product_id: int) -> None:
        return self.repository.delete_product(product_id)
