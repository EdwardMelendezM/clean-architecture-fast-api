import unittest
from infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository import MySQLProductsRepository
from domain.products_entities import CreateBodyProduct, UpdateBodyProduct


class TestMySQLProductsRepository(unittest.TestCase):
    # Reemplaza 'tu_db_url' con la URL de tu base de datos MySQL
    db_url = 'tu_db_url'

    def setUp(self):
        self.repository = MySQLProductsRepository(self.db_url)

    def test_get_products(self):
        products = self.repository.get_products()
        self.assertIsInstance(products, list)

    def test_get_product_by_id(self):
        # Asegúrate de tener al menos un producto en tu base de datos antes de ejecutar esta prueba
        product_id = 1
        product = self.repository.get_product_by_id(product_id)
        self.assertIsNone(product)  # Actualiza esto si tienes un producto con el ID específico

    def test_create_product(self):
        product_body = CreateBodyProduct(name='Test Product', price=10.99, description='Test Description')
        product = self.repository.create_product(product_body)
        self.assertIsNotNone(product.product_id)

    def test_update_product(self):
        # Asegúrate de tener al menos un producto en tu base de datos antes de ejecutar esta prueba
        product_id = 1
        update_body = UpdateBodyProduct(name='Updated Product', price=19.99, description='Updated Description')
        updated_product = self.repository.update_product(product_id, update_body)
        self.assertIsNotNone(updated_product)

    def test_delete_product(self):
        # Asegúrate de tener al menos un producto en tu base de datos antes de ejecutar esta prueba
        product_id = 1
        self.repository.delete_product(product_id)
        deleted_product = self.repository.get_product_by_id(product_id)
        self.assertIsNone(deleted_product)


if __name__ == '__main__':
    unittest.main()
