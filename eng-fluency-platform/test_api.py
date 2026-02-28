import urllib.request
import json

try:
    with urllib.request.urlopen("http://localhost:8000/api/v1/openapi.json") as response:
        data = json.loads(response.read().decode())
        paths = data.get("paths", {})
        if "/api/v1/register" in paths:
             print("FOUND /api/v1/register")
        elif "/register" in paths:
             print("FOUND /register")
        else:
             print("NOT FOUND /register")
             print("Available paths:", list(paths.keys()))
except Exception as e:
    print(f"Error: {e}")
