

from datetime import datetime
from zoneinfo import ZoneInfo


def to_colombia_time(dt: datetime) -> datetime:
    # Asegura que el datetime tenga zona UTC antes de convertirlo
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=ZoneInfo("UTC"))
    return dt.astimezone(ZoneInfo("America/Bogota"))
