import unittest
from unittest.mock import patch, Mock
from infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository import SqlAlchemyProductsRepository
from domain.products_entities import CreateBodyProduct, UpdateBodyProduct


class TestMySQLProductsRepository(unittest.TestCase):
    db_user = "root"
    db_password = "dev001001seguro"
    db_host = "127.0.0.1"
    db_port = 3306
    db_name = "db_test"

    db_url = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    def setUp(self):
        self.repository = SqlAlchemyProductsRepository(self.db_url)

    @patch('infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository.create_engine')
    @patch('infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository.sessionmaker')
    def test_get_products_success(self, sessionmaker_mock, create_engine_mock):
        # Mockear create_engine y sessionmaker
        create_engine_mock.return_value = Mock()
        session_mock = Mock()
        sessionmaker_mock.return_value = session_mock

        # Ejecutar la prueba
        products = self.repository.get_products()

        # Assertions
        self.assertIsInstance(products, list)

    @patch('infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository.create_engine')
    @patch('infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository.sessionmaker')
    def test_get_products_error(self, sessionmaker_mock, create_engine_mock):
        # Mockear create_engine y sessionmaker
        create_engine_mock.return_value = Mock(side_effect=Exception("Database error"))
        session_mock = Mock()
        sessionmaker_mock.return_value = session_mock

        # Ejecutar la prueba y verificar que se lance una excepción
        with self.assertRaises(Exception):
            self.repository.get_products()

    @patch('infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository.create_engine')
    @patch('infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository.sessionmaker')
    def test_get_product_by_id(self, sessionmaker_mock, create_engine_mock):
        # Mockear create_engine y sessionmaker
        create_engine_mock.return_value = Mock()
        session_mock = Mock()
        sessionmaker_mock.return_value = session_mock

        # Ejecutar la prueba
        product_id = 1
        product = self.repository.get_product_by_id(product_id)

        # Assertions
        self.assertIsNone(product)

    @patch('infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository.create_engine')
    @patch('infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository.sessionmaker')
    def test_create_product(self, sessionmaker_mock, create_engine_mock):
        # Mockear create_engine y sessionmaker
        create_engine_mock.return_value = Mock()
        session_mock = Mock()
        sessionmaker_mock.return_value = session_mock

        # Ejecutar la prueba
        product_body = CreateBodyProduct(name='Test Product', price=10.99, description='Test Description')
        product = self.repository.create_product(product_body)

        # Assertions
        self.assertIsNotNone(product.product_id)

    @patch('infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository.create_engine')
    @patch('infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository.sessionmaker')
    def test_update_product(self, sessionmaker_mock, create_engine_mock):
        # Mockear create_engine y sessionmaker
        create_engine_mock.return_value = Mock()
        session_mock = Mock()
        sessionmaker_mock.return_value = session_mock

        # Ejecutar la prueba
        product_id = 1
        update_body = UpdateBodyProduct(name='Updated Product', price=19.99, description='Updated Description')
        updated_product = self.repository.update_product(product_id, update_body)

        # Assertions
        self.assertIsNotNone(updated_product)

    @patch('infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository.create_engine')
    @patch('infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository.sessionmaker')
    def test_delete_product(self, sessionmaker_mock, create_engine_mock):
        # Mockear create_engine y sessionmaker
        create_engine_mock.return_value = Mock()
        session_mock = Mock()
        sessionmaker_mock.return_value = session_mock

        # Ejecutar la prueba
        product_id = 1
        self.repository.delete_product(product_id)
        deleted_product = self.repository.get_product_by_id(product_id)

        # Assertions
        self.assertIsNone(deleted_product)


if __name__ == '__main__':
    unittest.main()
