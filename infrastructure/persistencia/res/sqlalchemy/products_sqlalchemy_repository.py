from typing import List, Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.products_entities import Product, CreateBodyProduct, UpdateBodyProduct
from domain.products_repository import ProductsRepository
from infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_model import Base, ProductEntity
from infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_helper import _map_entity_to_domain


class SqlAlchemyProductsRepository(ProductsRepository):
    def __init__(self, db_url):
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def get_products(self) -> List[Product]:
        with self.Session() as session:
            products = session.query(ProductEntity).all()
            return [_map_entity_to_domain(product) for product in products]

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        with self.Session() as session:
            product_entity = session.query(ProductEntity).filter_by(product_id=product_id).first()
            return _map_entity_to_domain(product_entity) if product_entity else None

    def create_product(self, product_body: CreateBodyProduct) -> Product:
        with self.Session() as session:
            new_product = ProductEntity(name=product_body.name, price=int(product_body.price),
                                        description=product_body.description)
            session.add(new_product)
            session.commit()
            return _map_entity_to_domain(new_product)

    def update_product(self, product_id: int, update_body: UpdateBodyProduct) -> Optional[Product]:
        with self.Session() as session:
            product_entity = session.query(ProductEntity).filter_by(product_id=product_id).first()
            if product_entity:
                product_entity.name = update_body.name
                product_entity.price = float(update_body.price)
                product_entity.description = update_body.description
                session.commit()
                return _map_entity_to_domain(product_entity)
            else:
                return None

    def delete_product(self, product_id: int) -> None:
        with self.Session() as session:
            product_entity = session.query(ProductEntity).filter_by(product_id=product_id).first()
            if product_entity:
                session.delete(product_entity)
                session.commit()
