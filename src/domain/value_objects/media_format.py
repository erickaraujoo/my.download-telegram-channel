from telethon.tl.types import TypeMessageMedia, MessageMediaPhoto, MessageMediaDocument

MEDIA_FORMATS = {MessageMediaPhoto: ".jpg", MessageMediaDocument: ".mp4"}

def get_media_extension(media: TypeMessageMedia) -> str:
    for media_type, ext in MEDIA_FORMATS.items():
        if isinstance(media, media_type):
            return ext
    return None