from app.data.products import products

def retrieve_relevant_products(user_query: str):
    relevant = []

    for product in products:
        if (
            product["name"].lower() in user_query.lower()
            or product["brand"].lower() in user_query.lower()
        ):
            relevant.append(product)

    # If no direct match, return all products (fallback)
    if not relevant:
        return products

    return relevant