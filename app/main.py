from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from .aliexpress import get_aliexpress_products, get_product_details
from .cache import cache
import logging

app = FastAPI(title="AliExpress Aggregator API")

logging.basicConfig(level=logging.INFO)

@app.get("/products/")
async def search_products(query: str = Query(..., min_length=2)):
    try:
        if cached := cache.get(query):
            logging.info(f"Cache hit for query: {query}")
            return JSONResponse(content=cached)

        products = get_aliexpress_products(query)
        cache.set(query, products)
        return JSONResponse(content=products)

    except Exception as e:
        logging.error(f"Error while searching products: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.get("/products/{product_id}")
async def get_product(product_id: str):
    try:
        if cached := cache.get(product_id):
            logging.info(f"Cache hit for product ID: {product_id}")
            return JSONResponse(content=cached)

        product = get_product_details(product_id)
        cache.set(product_id, product)
        return JSONResponse(content=product)

    except Exception as e:
        logging.error(f"Error getting product: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.get("/health")
async def health_check():
    return {"status": "ok"}