import requests
BASE_URL = "https://example.com/api/cart"

def add_to_cart(product_id:int, quantity: int):
    try:
        response = requests.post(f"{BASE_URL}/add", json = {"product_id": product_id, "quantity": quantity})
        response.raise_for_status()
        return response.json()
    
    except requests.RequestException as e:
        return {"error": str(e)}
    
def remove_from_cart(product_id: int):
    try:
        response = requests.post(f"{BASE_URL}/remove", json={"product_id": product_id})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
    
def view_cart():
    try:
        response = requests.get(f"{BASE_URL}/view")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
