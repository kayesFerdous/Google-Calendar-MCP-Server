from datetime import datetime
from typing import Optional

from src.schemas.calendar_event import CalendarEvent as Event, EventDateTime
from src.events.create_event import insert_event


def create_google_calendar_event(
    summary: str,
    start: datetime,
    end: datetime,
    description: Optional[str] = None,
    location: Optional[str] = None,
    time_zone: str = "Asia/Dhaka",
) -> str:
    """
    Create a new event in Google Calendar.

    Args:
        summary (str):                  The summary or title of the event.

        start (nested object):          The start time of the event in RFC3339 format (e.g., '2025-08-07T14:00:00Z').
                                        This is a nested object with a `dateTime` and `timeZone`.

        end(nested object):             The end time of the event in RFC3339 format (e.g., '2025-08-07T15:30:00Z').
                                        This is a nested object with a `dateTime` and `timeZone`.

        description (str, optional):    A description of the event. Can contain HTML. Defaults to "".

        location (str, optional):       Geographic location of the event as free-form text. Defaults to "".

        time_zone (str):                The timezone for the event. Defaults to "UTC".

    Returns:
        str: The HTML link of the created event.
    """

    event_model = Event(
        summary=summary,
        location=location,
        description=description,
        start=EventDateTime(dateTime=start, timeZone=time_zone),
        end=EventDateTime(dateTime=end, timeZone=time_zone),
    )

    created_event = insert_event(event_model)
    html_link = created_event.get("htmlLink") or "Event created"
    return html_link
