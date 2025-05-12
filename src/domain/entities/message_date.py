import pytz
from datetime import datetime

class MessageDate:
    def __init__(
        self,
        str: str,
        year: str,
        month: str,
        day: str,
        hour: str,
        minute: str,
        second: str,
    ):
        self.str = str
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second


def get_message_date(date: datetime) -> MessageDate:
    utc = date.astimezone(pytz.utc)
    message_time = utc.astimezone(pytz.timezone("America/Sao_Paulo"))
    str = message_time.strftime("%Y-%m-%d %H:%M:%S")
    year = message_time.strftime("%Y")
    month = message_time.strftime("%m")
    day = message_time.strftime("%d")
    hour = message_time.strftime("%H")
    minute = message_time.strftime("%M")
    second = message_time.strftime("%S")

    return MessageDate(str, year, month, day, hour, minute, second)
