from telethon.tl.types import TypeMessageMedia, MessageMediaPhoto, MessageMediaDocument

MEDIA_TYPE_PATHS = {MessageMediaPhoto: "images", MessageMediaDocument: "videos"}

def get_media_type_path(media: TypeMessageMedia) -> str:
    for media_type, path in MEDIA_TYPE_PATHS.items():
        if isinstance(media, media_type):
            return path
    return None
  
def get_media_name(channel_keyword: str, id: int, extension: str) -> str:
  return f"{channel_keyword}_{id}{extension}"