from flask import Flask, request

app = Flask(__name__)

# Завдання 2: Простий GET-запит
@app.route("/")
def hello_world():
    return "Hello World!"

# Завдання 3: GET-запит з параметром
@app.route("/currency")
def currency():
    # Отримати параметр "today" з URL
    param = request.args.get('today')
    if param:
        return f"USD - 41.5 (today: {param})"
    return "USD - 41.5"

if __name__ == '__main__':
    app.run(port=8000)
