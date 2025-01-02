from flask import Flask, request

app = Flask(__name__)

@app.route("/save", methods=["POST"])
def save_to_file():
    # Отримуємо дані з тіла запиту
    data = request.data.decode("utf-8")
    # Записуємо у файл
    with open("data.txt", "a") as file:
        file.write(data + "\n")
    return "Data saved to file!", 200

if __name__ == '__main__':
    app.run(port=8000)
