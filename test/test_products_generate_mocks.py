# test_products.py

from unittest.mock import Mock
from domain.products_repository import ProductsRepository
from domain.products_usecase import ProductsUseCase


def test_products_repository(mocker):
    # Mockear la clase ProductsRepository y sus métodos
    mocker.patch('domain.products_repository.ProductsRepository', Mock)

    # Crear una instancia del mock
    products_repository_mock = ProductsRepository()

    # Realizar tus pruebas con products_repository_mock


def test_products_use_case(mocker):
    # Mockear la clase ProductsUseCase y sus métodos
    mocker.patch('domain.products_usecase.ProductsUseCase', Mock)

    # Crear una instancia del mock
    products_use_case_mock = ProductsUseCase()

    # Realizar tus pruebas con products_use_case_mock
