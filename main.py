from fastapi import FastAPI
from infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository import SqlAlchemyProductsRepository
from usecase.products_usecase import ProductsUCase
from interface import products_handler

app = FastAPI()
db_url = ""

products_repository = SqlAlchemyProductsRepository(db_url)
products_use_case = ProductsUCase(products_repository)
products_handler = products_handler.ProductsHandler(app, products_repository, products_use_case)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
