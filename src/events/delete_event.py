from src.service import get_calendar_service
from src.events.get_events import get_events
from src.schemas.events_query import ListEventsParams


def delete_events(event_name: str = "") -> str:

    if not event_name:
        return "Event name was not given"

    events = get_events(ListEventsParams(maxResults=250))

    if len(events) == 0:
        return "No events were found"

    event_id = None
    for event in events:
        if event.get("summary") == event_name:
            event_id = event.get("id")
            break

    if not event_id:
        return f"event: {event_name} was not found"

    try:
        service = get_calendar_service()
        service.events().delete(calendarId="primary", eventId=event_id).execute()
        return f"successfully deleted the event: {event_name}"
    except Exception:
        return f"Error deleting the event: {event_name}"
