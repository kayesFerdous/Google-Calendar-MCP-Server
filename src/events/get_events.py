from src.schemas.events_query import ListEventsParams
from src.service import get_calendar_service


def get_events(event_args: ListEventsParams):

    service = get_calendar_service()

    event_args_json = event_args.model_dump(exclude_none=True, mode="json")

    events_result = (
        service.events()
        .list(**event_args_json)
        .execute()
    )
    
    events = events_result.get("items", [])

    if not events:
      return []
    
    return events

