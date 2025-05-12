import os
from src.domain.entities.message_date import MessageDate
from src.domain.value_objects.media_path import get_media_type_path
from telethon.tl.types import TypeMessageMedia


def create_channel_path(
    message_date: MessageDate,
    media: TypeMessageMedia,
    keyword: str,
) -> str:
    media_type_path = get_media_type_path(media=media)
    channel_path = f"downloads\\{keyword}\\{message_date.year}\\{message_date.month}\\{media_type_path}"

    os.makedirs(channel_path, exist_ok=True)

    return channel_path


def get_media_path(channel_path: str, media_name: str) -> str:
    return f"{channel_path}\\{media_name}"
