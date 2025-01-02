from telethon import TelegramClient
from dotenv import load_dotenv
import os

# Завантажуємо змінні з .env файлу
load_dotenv('config.env')

# Зчитуємо API ID та API Hash з .env файлу
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# Зчитуємо chat_username та message з .env файлу
chat_username = os.getenv('USERNAME_OR_LINK')
message = os.getenv('MESSAGE')

# Налаштування клієнта
client = TelegramClient('session_name', api_id, api_hash)

# Функція для відправки повідомлення
async def send_message():
    try:
        # Підключення до Telegram
        await client.start()

        # Відправка повідомлення
        await client.send_message(chat_username, message)

        print(f"Повідомлення надіслано до {chat_username}!")

    except Exception as e:
        print(f"Сталася помилка: {e}")
    finally:
        await client.disconnect()

# Викликаємо функцію для відправки повідомлення
with client:
    client.loop.run_until_complete(send_message())
