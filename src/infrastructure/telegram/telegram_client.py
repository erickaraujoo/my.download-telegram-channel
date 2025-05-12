import os
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()


async def get_telegram_client() -> TelegramClient:
    api_id = int(os.getenv("API_ID"))
    api_hash = os.getenv("API_HASH")
    phone_number = os.getenv("PHONE_NUMBER")

    client = TelegramClient("session_name", api_id, api_hash)

    await client.start(phone=phone_number)

    return client
