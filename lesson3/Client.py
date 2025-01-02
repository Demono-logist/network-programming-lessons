import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:5000"
AUTH = HTTPBasicAuth("admin", "password123")

# Get all items
response = requests.get(f"{BASE_URL}/items", auth=AUTH)
print("GET /items:", response.json())

# Add a new item
new_item = {"id": 4, "name": "Excelsa", "price": 130.00}
response = requests.post(f"{BASE_URL}/items", json=new_item, auth=AUTH)
print("POST /items:", response.json())

# Get specific item
response = requests.get(f"{BASE_URL}/items/4", auth=AUTH)
print("GET /items/4:", response.json())

# Update an item
update_item = {"name": "Excelsa Deluxe", "price": 140.00}
response = requests.put(f"{BASE_URL}/items/4", json=update_item, auth=AUTH)
print("PUT /items/4:", response.json())

# Delete an item
response = requests.delete(f"{BASE_URL}/items/4", auth=AUTH)
print("DELETE /items/4:", response.json())
