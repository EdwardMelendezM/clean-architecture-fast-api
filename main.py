from interface import products_handler

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(products_handler.app, host="127.0.0.1", port=8000, reload=True)
