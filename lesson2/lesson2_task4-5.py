from flask import Flask, request, jsonify, Response
import requests

app = Flask(__name__)

# Завдання 4: Обробка заголовків запиту
@app.route("/content", methods=["GET"])
def handle_content_type():
    content_type = request.headers.get("Content-Type")
    
    if content_type == "application/json":
        return jsonify({"message": "Hello, this is a JSON response!"})
    elif content_type == "application/xml":
        return Response("<message>Hello, this is an XML response!</message>", mimetype="application/xml")
    else:
        return "Hello, this is a plain text response!"

# Завдання 5: Динамічний курс валют
@app.route("/currency", methods=["GET"])
def get_currency():
    param = request.args.get("param")
    nbu_api_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
    params = {"valcode": "USD", "json": ""}
    
    if param == "today":
        response = requests.get(nbu_api_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return jsonify({"USD": data[0]["rate"], "date": data[0]["exchangedate"]})
        return "Error fetching data from NBU API.", 500

    elif param == "yesterday":
        # Отримати вчорашню дату
        from datetime import datetime, timedelta
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
        response = requests.get(nbu_api_url, params={**params, "date": yesterday})
        if response.status_code == 200:
            data = response.json()
            return jsonify({"USD": data[0]["rate"], "date": data[0]["exchangedate"]})
        return "Error fetching data from NBU API.", 500

    else:
        return "Invalid parameter. Use 'today' or 'yesterday'.", 400

if __name__ == '__main__':
    app.run(port=8000)
