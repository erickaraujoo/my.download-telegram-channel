import os
from telethon.tl.types import Channel, Message
from telethon import TelegramClient
from src.domain.enums.channel_keyword import ChannelKeyword
from src.domain.entities.message_content import get_message_content
from src.domain.value_objects.media_format import get_media_extension
from src.domain.entities.message_content import get_message_content
from src.domain.value_objects.media_path import get_media_name
from src.infrastructure.file_system.media_storage import (
    create_channel_path,
    get_media_path,
)
from typing import cast


def download_media_progress(current, total):
    porc = int(current * 100 / total)
    print(f"\r📥 Progresso: {porc}% ({current}/{total} bytes)", end=" ")


async def download_media(message: Message, media_path: str) -> str:
    saved_path = await message.download_media(
        file=media_path, progress_callback=download_media_progress
    )

    return saved_path


async def download_media_usecase(
    client: TelegramClient,
    channel: Channel,
    channel_keyword: ChannelKeyword,
    channel_name: str,
):
    async for message in client.iter_messages(channel):
        typed_message = cast(Message, message)
        message_content = get_message_content(message=typed_message)

        if not message_content.media:
            continue

        media_extension = get_media_extension(media=message_content.media)

        if media_extension is None:
            continue

        media_name = get_media_name(
            channel_keyword=channel_keyword.name.lower(),
            id=message_content.id,
            extension=media_extension,
        )

        channel_path = create_channel_path(
            message_date=message_content.date,
            media=message_content.media,
            keyword=channel_keyword.name.lower(),
        )

        media_path = get_media_path(channel_path=channel_path, media_name=media_name)

        if os.path.exists(media_path):
            print(f"✔️  Canal {channel_name} atualizado com sucesso!")
            break

        downloaded_media = await download_media(
            message=typed_message, media_path=media_path
        )

        print(
            f"[{message_content.date.str}] --> ✔️  Mídia baixada com sucesso: {downloaded_media}"
        )
    else:
        raise Exception(f"❌ Erro durante o download de mensagens!")
