from fastapi import FastAPI
from domain.products_repository import ProductsRepository
from domain.products_usecase import ProductsUseCase
from interface import products_handler

if __name__ == "__main__":
    import uvicorn

    app = FastAPI()
    db_url = "sqlite:///db.sqlite3"
    products_repository = ProductsRepository(db_url)
    products_use_case = ProductsUseCase(products_repository)
    products_handler = products_handler.ProductsHandler(app, products_repository, products_use_case)
    uvicorn.run(products_handler.app, host="127.0.0.1", port=8000, reload=True)
