from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
import json

app = Flask(__name__)
auth = HTTPBasicAuth()

# Simple user authentication (can be extended to file or database)
users = {
    "admin": "password123",
    "user": "pass456"
}

@auth.get_password
def get_password(username):
    return users.get(username)

# Path to JSON file for storing catalog data
CATALOG_FILE = 'catalog.json'

# Load catalog from file or initialize empty catalog
def load_catalog():
    try:
        with open(CATALOG_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save catalog to file
def save_catalog(catalog):
    with open(CATALOG_FILE, 'w') as f:
        json.dump(catalog, f, indent=4)

# Initialize catalog
catalog = load_catalog()

@app.route('/items', methods=['GET', 'POST'])
@auth.login_required
def manage_items():
    if request.method == 'GET':
        return jsonify(catalog), 200
    elif request.method == 'POST':
        data = request.json
        if not all(key in data for key in ("id", "name", "price")):
            return jsonify({"error": "Missing required fields"}), 400

        item_id = str(data['id'])
        if item_id in catalog:
            return jsonify({"error": "Item with this ID already exists"}), 400

        catalog[item_id] = {
            "name": data["name"],
            "price": data["price"]
        }
        save_catalog(catalog)
        return jsonify({"message": "Item added successfully"}), 201

@app.route('/items/<id>', methods=['GET', 'PUT', 'DELETE'])
@auth.login_required
def manage_item(id):
    item_id = str(id)

    if request.method == 'GET':
        item = catalog.get(item_id)
        if item is None:
            return jsonify({"error": "Item not found"}), 404
        return jsonify(item), 200

    elif request.method == 'PUT':
        if item_id not in catalog:
            return jsonify({"error": "Item not found"}), 404

        data = request.json
        catalog[item_id].update({
            "name": data.get("name", catalog[item_id]["name"]),
            "price": data.get("price", catalog[item_id]["price"])
        })
        save_catalog(catalog)
        return jsonify({"message": "Item updated successfully"}), 200

    elif request.method == 'DELETE':
        if item_id not in catalog:
            return jsonify({"error": "Item not found"}), 404

        del catalog[item_id]
        save_catalog(catalog)
        return jsonify({"message": "Item deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
