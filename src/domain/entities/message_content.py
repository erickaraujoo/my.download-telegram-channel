from src.domain.entities.message_date import MessageDate, get_message_date
from telethon.tl.types import TypeMessageMedia, Message


class MessageContent:
    def __init__(
        self, id: int, date: MessageDate, text: str, media: TypeMessageMedia | None
    ):
        self.id = id
        self.date = date
        self.text = text
        self.media = media


def get_message_content(message: Message) -> MessageContent:
    id = message.id
    date = get_message_date(date=message.date)
    text = message.text
    media = message.media

    return MessageContent(id, date, text, media)
