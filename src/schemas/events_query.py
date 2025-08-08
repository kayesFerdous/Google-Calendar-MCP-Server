from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ListEventsParams(BaseModel):
    """
    Parameters for listing Google Calendar events via events.list.
    """

    calendarId: str = "primary"
    maxResults: int = 5
    orderBy: Optional[str] = "startTime"
    singleEvents: bool = True
    timeMin: Optional[datetime] = None
    timeMax: Optional[datetime] = None
    timeZone: Optional[str] = None


