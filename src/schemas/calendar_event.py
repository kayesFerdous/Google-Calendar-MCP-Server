from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from pydantic.config import ConfigDict


class EventDateTime(BaseModel):
    """
    Represents the start or end time of a Google Calendar event.
    """

    dateTime: datetime
    timeZone: Optional[str] = None


class Attendee(BaseModel):
    """
    Represents an attendee of a Google Calendar event.
    """

    email: str


class ReminderOverride(BaseModel):
    """
    Represents a reminder override for a Google Calendar event.
    """

    method: str
    minutes: int


class Reminders(BaseModel):
    """
    Represents the reminders for a Google Calendar event.
    """

    useDefault: bool
    overrides: Optional[List[ReminderOverride]] = None


class CalendarEvent(BaseModel):
    """
    Represents a Google Calendar event.
    """

    summary: str
    location: Optional[str] = None
    description: Optional[str] = None
    start: EventDateTime
    end: EventDateTime
    attendees: Optional[List[Attendee]] = None
    reminders: Optional[Reminders] = None

    model_config = ConfigDict(from_attributes=True)


