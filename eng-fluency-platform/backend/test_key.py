import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GOOGLE_API_KEY")
print(f"Testing Key: {key[:10]}...")

genai.configure(api_key=key)

try:
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content("Hello")
    print("Chat Test Success!")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Chat Test Failure: {e}")
