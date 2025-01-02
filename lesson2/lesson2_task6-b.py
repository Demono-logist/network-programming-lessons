import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Ініціалізація бази даних
def init_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/save", methods=["POST"])
def save_to_db():
    # Отримуємо дані з тіла запиту
    data = request.data.decode("utf-8")
    
    # Зберігаємо у базу даних
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data (content) VALUES (?)", (data,))
    conn.commit()
    conn.close()
    
    return "Data saved to database!", 200

if __name__ == '__main__':
    init_db()  # Створення таблиці, якщо її немає
    app.run(port=8000)
