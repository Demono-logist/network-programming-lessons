from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# Завантажуємо змінні з .env файлу
load_dotenv('config.env')

# Дані Telegram API
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# Посилання на чат
chat_public_link = os.getenv('CHAT_PUBLIC_USERNAME')

with TelegramClient('session_name', api_id, api_hash) as client:
    # Отримання об'єкта чату
    chat_entity = client.get_entity(chat_public_link)

    # Ініціалізація параметрів
    all_participants = []
    offset = 0
    limit = 150

    # Отримання списку учасників
    while True:
        participants = client(GetParticipantsRequest(
            channel=chat_entity,
            filter=ChannelParticipantsSearch(''),
            offset=offset,
            limit=limit,
            hash=0  # Встановлюємо hash як 0
        ))
        all_participants.extend(participants.users)
        if not participants.users:
            break
        offset += len(participants.users)

    # Вивід списку учасників
    for participant in all_participants:
        print(f"ID: {participant.id}, Username: {participant.username}, Name: {participant.first_name}")
