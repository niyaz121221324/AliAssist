from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from .aliexpress import get_aliexpress_products

app = FastAPI(title="AliExpress Aggregator API")

@app.get("/products/")
async def search_products(query: str = Query(..., min_length=2)):
    try:
        products = get_aliexpress_products(query)
        return JSONResponse(content=products)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
