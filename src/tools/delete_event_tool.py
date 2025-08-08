from src.events.delete_event import delete_events


def delete_google_calendar_event(event_name: str) -> str:
    """Delete an event by exact summary match from Google Calendar."""
    return delete_events(event_name)

