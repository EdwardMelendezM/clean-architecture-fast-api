from domain.products_entities import Product
from infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_model import ProductEntity


def _map_entity_to_domain(product_entity: ProductEntity) -> Product:
    return Product(
        product_id=product_entity.product_id,
        name=product_entity.name,
        price=product_entity.price,
        description=product_entity.description
    )
