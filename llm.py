import os
from typing import Optional
from dotenv import load_dotenv
import google.generativeai as genai
from pydantic import BaseModel
import json

load_dotenv()

# 1. Define the Response Schema using Pydantic
class RetailResponse(BaseModel):
    intent: str
    product_name: Optional[str] = None
    quantity: Optional[int] = 1
    category: Optional[str] = None
    price_limit: Optional[float] = None
    order_id: Optional[str] = None
    answer: Optional[str] = None

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 2. System Prompt
SYSTEM_PROMPT = """
You are an AI Retail Business Agent. Your job is to categorize user messages into one of the following intents and extract the details.

INTENT RULES:
- 'place_order': Use when the user wants to buy, purchase, or order a specific item.
- 'product_search': Use when the user wants to find, see, browse, or search for items. Even if they just say "I am searching for{product}," use this.
- 'stock_check': Use when the user asks if an item is available or how many are left.
- 'order_status': Use when the user asks about their previous purchases or "what did I buy?"
- 'general_query': Use ONLY for greetings (hello) or questions that don't involve products.

You must respond with valid JSON only, in this exact format:
{
    "intent": "one of the intents above",
    "product_name": "product name or null",
    "quantity": number or 1,
    "category": "category or null",
    "price_limit": number or null,
    "order_id": "order id or null",
    "answer": "answer text or null"
}
"""

def process_message(user_message: str):
    try:
        # Create the model with system instruction
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash-lite",
            system_instruction=SYSTEM_PROMPT,
            generation_config={
                "temperature": 0.3,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 1024,
            }
        )
        
        # Generate content
        response = model.generate_content(user_message)
        
        # Parse the JSON response
        response_text = response.text.strip()
        
        # Remove markdown code blocks if present
        if response_text.startswith('```json'):
            response_text = response_text[7:]
        if response_text.startswith('```'):
            response_text = response_text[3:]
        if response_text.endswith('```'):
            response_text = response_text[:-3]
        
        response_text = response_text.strip()
        
        # Parse JSON
        response_data = json.loads(response_text)
        
        # Return as RetailResponse object
        return RetailResponse(**response_data)

    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        print(f"Response text was: {response_text}")
        return RetailResponse(intent="error", answer="I couldn't understand that properly. Could you rephrase?")
    
    except Exception as e:
        print(f"Error in LLM processing: {e}")
        return RetailResponse(intent="error", answer="I encountered an error processing that.")