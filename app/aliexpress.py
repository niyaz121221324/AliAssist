import requests

RAPIDAPI_KEY = "708b2a8b97msh1629e0bebcfc5fcp1aa461jsnf68afc6f5a0d"
HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "ali-express1.p.rapidapi.com"
}

def get_aliexpress_products(query: str):
    url = "https://ali-express1.p.rapidapi.com/search"
    params = {"query": query, "page": "1"}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def get_product_details(product_id: str):
    url = f"https://ali-express1.p.rapidapi.com/product/{product_id}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()