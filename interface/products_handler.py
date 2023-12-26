from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

from domain.products_entities import Product, CreateBodyProduct, UpdateBodyProduct, PaginatedProductList
from domain.products_repository import ProductsRepository
from domain.products_usecase import ProductsUseCase


class ProductsHandler:
    def __init__(self, app: FastAPI, products_repository: ProductsRepository,
                 products_use_case: ProductsUseCase):
        self.app = app
        self.products_repository = products_repository
        self.products_use_cases = products_use_case

        self.setup_routes()

    def setup_routes(self):
        @self.app.get('/products', response_model=PaginatedProductList)
        def get_products(page: int = Query(1, gt=0), size_page: int = Query(10, gt=0, le=100)):
            all_products = self.products_use_cases.get_products()
            start_idx = (page - 1) * size_page
            end_idx = start_idx + size_page
            return PaginatedProductList(items=all_products[start_idx:end_idx], total_items=len(all_products))

        @self.app.get('/products/{product_id}', response_model=Product)
        def get_product(product_id: int):
            product = self.products_use_cases.get_product_by_id(product_id)
            if product:
                return product
            else:
                raise HTTPException(status_code=404, detail="Product not found")

        @self.app.post('/products', response_model=Product, status_code=201)
        def create_product(product_body: CreateBodyProduct):
            try:
                new_product = self.products_use_cases.create_product(product_body)
                return new_product
            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))

        @self.app.put('/products/{product_id}', response_model=Product)
        def update_product(product_id: int, update_body: UpdateBodyProduct):
            updated_product = self.products_use_cases.update_product(product_id, update_body)
            if updated_product:
                return updated_product
            else:
                raise HTTPException(status_code=404, detail="Product not found")

        @self.app.delete('/products/{product_id}', status_code=200)
        def delete_product(product_id: int):
            self.products_use_cases.delete_product(product_id)
            return JSONResponse(content={"message": "Product deleted successfully"})
