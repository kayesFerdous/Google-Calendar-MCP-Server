from typing import Any, Dict

from src.schemas.calendar_event import CalendarEvent as Event
from src.service import get_calendar_service


def insert_event(created_event: Event) -> Dict[str, Any]:
    """
    Insert an event into the primary Google Calendar and return the API response.
    """
    event_dict = created_event.model_dump(exclude_none=True, mode="json")
    service = get_calendar_service()
    result = service.events().insert(calendarId="primary", body=event_dict).execute()
    return result


