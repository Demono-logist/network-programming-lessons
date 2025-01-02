from bottle import route, run, request

# Завдання 2: Простий GET-запит
@route("/")
def hello():
    return "Hello World!"

# Завдання 3: GET-запит з параметром
@route("/currency")
def currency():
    # Отримати параметр "today" з URL
    param = request.query.today
    if param:
        return f"USD - 41.5 (today: {param})"
    return "USD - 41.5"

if __name__ == '__main__':
    run(host='localhost', port=8000)
