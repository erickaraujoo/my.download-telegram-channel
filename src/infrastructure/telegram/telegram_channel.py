from telethon import TelegramClient
from telethon.tl.types import Channel

async def get_telegram_channel(client: TelegramClient, channel_name: str) -> Channel:
    async for dialog in client.iter_dialogs():
        if dialog.name == channel_name:
            return dialog.entity
    else:
        raise Exception(f"❌ Grupo '{channel_name}' não encontrado!")
