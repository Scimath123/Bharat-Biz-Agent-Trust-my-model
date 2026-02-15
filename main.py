from fastapi import FastAPI
from llm import process_message  
from database import get_connection, create_tables
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB on startup
create_tables()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(chat_request: ChatRequest):
    # 1. Get structured AI response
    ai_data = process_message(chat_request.message)

    # Database setup
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # 🛒 PLACE ORDER
        if ai_data.intent == "place_order":
            product = ai_data.product_name
            qty = ai_data.quantity or 1

            if not product:
                return {"reply": "I understood you want to order, but what product?"}

            
            cursor.execute("""
                SELECT id, price, name
                FROM products
                WHERE LOWER(name) LIKE LOWER(%s)
                LIMIT 1
            """, (f"%{product}%",))

            item = cursor.fetchone()

            if not item:
                return {"reply": f"Sorry, we don't carry '{product}' in our catalog."}

            # Insert Order
            cursor.execute("""
                INSERT INTO orders (product_id, quantity, price_at_sale)
                VALUES (%s, %s, %s)
            """, (item["id"], qty, item["price"]))

            conn.commit() 
            
           
            return {"reply": f"Success! Ordered {qty} {item['name']}(s) {item['id']}. Total: ${item['price'] * qty}"}

        # 🔍 PRODUCT SEARCH
        if ai_data.intent == "product_search":
            category = ai_data.category or ""
            
            cursor.execute("""
                SELECT id, name, price
                FROM products
                WHERE LOWER(name) LIKE LOWER(%s) OR LOWER(category) LIKE LOWER(%s) 
                ORDER BY id DESC
                LIMIT 5
            """, (f"%{category}%", f"%{category}%"))
            
            results = cursor.fetchall()
            if not results:
                return {"reply": "No matching products found."}
            return {"products": results}

        # 📦 STOCK/ORDER CHECK (Example of using JOIN to show names)
        if ai_data.intent == "order_status":
            # This query JOINS orders and products to show the name
            cursor.execute("""
                SELECT p.name, o.quantity, o.price_at_sale
                FROM orders o
                JOIN products p ON o.product_id = p.id
                ORDER BY o.id DESC
                LIMIT 5
            """)
            recent_orders = cursor.fetchall()
            return {"recent_orders": recent_orders}

       
        if ai_data.intent == "general_query":
            return {"reply": ai_data.answer or "How can I help you?"}

    finally:
        cursor.close()
        conn.close()

    return {"reply": "I'm not sure how to handle that yet."}
