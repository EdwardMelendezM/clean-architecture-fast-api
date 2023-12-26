from abc import ABC, abstractmethod
from typing import List, Optional

from products_entities import Product, CreateBodyProduct, UpdateBodyProduct


class ProductsUseCase(ABC):
    @abstractmethod
    def get_products(self) -> List[Product]:
        """
        Obtiene la lista completa de productos.

        :return: Lista de objetos Product.
        """
        pass

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """
        Obtiene un producto por su identificador único.

        :param product_id: Identificador único del producto.
        :return: Objeto Product si existe, None si no se encuentra.
        """
        pass

    @abstractmethod
    def create_product(self, product: CreateBodyProduct) -> Product:
        """
        Crea un nuevo producto.

        :param product: Datos del producto a crear.
        :return: Objeto Product recién creado.
        """
        pass

    @abstractmethod
    def update_product(self, product_id: int, update_body: UpdateBodyProduct) -> Optional[Product]:
        """
        Actualiza la información de un producto existente.

        :param product_id: Identificador único del producto a actualizar.
        :param update_body: Datos actualizados del producto.
        :return: Objeto Product actualizado si existe, None si no se encuentra.
        """
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> None:
        """
        Elimina un producto por su identificador único.

        :param product_id: Identificador único del producto a eliminar.
        """
        pass
