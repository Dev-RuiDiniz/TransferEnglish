import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")
print(f"Testing Key: {key}")
genai.configure(api_key=key)

try:
    print("\nModels:")
    for m in genai.list_models():
        print(f"Name: {m.name}")
except Exception as e:
    print(f"Error: {e}")
