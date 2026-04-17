# from fastapi import FastAPI
# from app.models.schemas import ChatRequest, ChatResponse
# from app.services.product_service import retrieve_relevant_products
# from app.services.ai_service import generate_ai_response

# app = FastAPI(title="AI Product Chatbot")

# @app.post("/chat", response_model=ChatResponse)
# async def chat(request: ChatRequest):

#     user_query = request.message

#     # Step 1: Retrieve relevant product data
#     relevant_products = retrieve_relevant_products(user_query)

#     # Step 2: Generate AI response
#     ai_response = generate_ai_response(user_query, relevant_products)

#     return ChatResponse(response=ai_response)

from fastapi import FastAPI
from app.models.schemas import ChatRequest, ChatResponse

# 1️⃣ Create FastAPI app
app = FastAPI()

# 2️⃣ Define your endpoint
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        user_query = request.message
        relevant_products = retrieve_relevant_products(user_query)
        ai_response = generate_ai_response(user_query, relevant_products)
        return ChatResponse(response=ai_response)
    except Exception as e:
        print("Error:", e)
        return ChatResponse(response=f"[ERROR] {str(e)}")