from fastapi import FastAPI
from infrastructure.persistencia.res.sqlalchemy.products_sqlalchemy_repository import SqlAlchemyProductsRepository
from usecase.products_usecase import ProductsUCase
from interface import products_handler

app = FastAPI()
db_user = "root"
db_password = "dev001001seguro"
db_host = "127.0.0.1"
db_port = 3306
db_name = "db_test"

db_url = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

products_repository = SqlAlchemyProductsRepository(db_url)
products_use_case = ProductsUCase(products_repository)
products_handler = products_handler.ProductsHandler(app, products_repository, products_use_case)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
