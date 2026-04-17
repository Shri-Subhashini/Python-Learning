# from openai import OpenAI
# from app.config import OPENAI_API_KEY

# client = OpenAI(api_key=OPENAI_API_KEY)

# def generate_ai_response(user_query: str, product_context: list):

#     prompt = f"""
#     You are a helpful e-commerce assistant.

#     Here are the product details:
#     {product_context}

#     Answer the user question based ONLY on the product information provided.
#     If the information is not available, say you don't have enough data.

#     User Question: {user_query}
#     """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a professional product assistant."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.3
#     )

#     return response.choices[0].message.content

# app/services/ai_service.py

def generate_ai_response(user_query: str, product_context: list):
    # Mock response for testing FastAPI endpoints
    return f"[MOCK] This is a response for: '{user_query}'"