import asyncio
from src.interface.cli.menu import show_menu
from src.config.constants import channel_names, download_type_names
from src.domain.enums.channel_keyword import ChannelKeyword
from src.domain.enums.download_keyword import DownloadKeyword
from src.application.usecases.download_media_usecase import download_media_usecase
from src.infrastructure.telegram.telegram_client import get_telegram_client
from src.infrastructure.telegram.telegram_channel import get_telegram_channel


async def telegram_channel_factory(
    channel_keyword: ChannelKeyword,
    channel_name: str,
    download_type_keyword: DownloadKeyword,
):
    telegram_client = await get_telegram_client()

    telegram_channel = await get_telegram_channel(
        client=telegram_client, channel_name=channel_name
    )

    await {
        DownloadKeyword.MEDIAS: lambda: download_media_usecase(
            client=telegram_client,
            channel=telegram_channel,
            channel_keyword=channel_keyword,
            channel_name=channel_name,
        )
    }[download_type_keyword]()


if __name__ == "__main__":
    channel_name = show_menu(
        message="Escolha qual canal deseja:",
        choices=[
            channel_names[0],
            channel_names[1],
            channel_names[2],
            channel_names[3],
        ],
    )

    download_type_name = show_menu(
        message="Escolha o tipo de download:",
        choices=[download_type_names[0]],
    )

    channel_keyword = ChannelKeyword(channel_name)
    download_type_keyword = DownloadKeyword(download_type_name)

    asyncio.run(
        telegram_channel_factory(
            channel_keyword=channel_keyword,
            channel_name=channel_name,
            download_type_keyword=download_type_keyword,
        )
    )
