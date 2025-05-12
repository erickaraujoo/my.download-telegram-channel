import unicodedata
import re
from enum import Enum
from src.config.constants import channel_names


def format_enum_key(name: str) -> str:
    name = unicodedata.normalize("NFKD", name).encode("ASCII", "ignore").decode()
    name = name.replace(" ", "_")
    name = re.sub(r"[^A-Za-z0-9_]", "", name)
    name = re.sub(r"_+", "_", name)
    name = name.strip("_")

    return name.upper()


channel_dict = {format_enum_key(name): name for name in channel_names}

ChannelKeyword = Enum("ChannelKeyword", channel_dict)
