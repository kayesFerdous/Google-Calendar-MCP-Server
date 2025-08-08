from datetime import datetime
from typing import Optional

from src.schemas.events_query import ListEventsParams
from src.events.get_events import get_events


def get_google_calendar_events(
    calendarId: str = "primary",
    maxResults: int = 5,
    orderBy: Optional[str] = "startTime",
    singleEvents: bool = True,
    timeMin: Optional[datetime] = None,
    timeMax: Optional[datetime] = None,
    timeZone: str = "Asia/Dhaka"
):
    """
    Gets all the events from the Google Calender.

    Args:
        calendarId (str, optional):     The calendar ID. Defaults to "primary".

        maxResults (int):               The maximum number of events to return.

        orderBy	(string):           	The order of the events returned in the result. Optional. The default is an unspecified, stable order. Acceptable values are:
                                        "startTime":    Order by the start date/time (ascending). This is only available when querying 
                                                        single events (i.e. the parameter singleEvents is True)
                                        "updated":      Order by last modification time (ascending).


        singleEvents (bool, optional):  Whether to expand recurring events. Defaults to True.

        timeMin (datatime):             Lower bound (exclusive) for an event's end time to filter by. Optional. The default is not to filter by end time.
                                        Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2025-06-03T10:00:00+06:00. 
                                        Milliseconds may be provided but are ignored. If timeMax is set, timeMin must be smaller than timeMax.

        timeMax (datetime): 	        Upper bound (exclusive) for an event's start time to filter by. Optional. 
                                        The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone 
                                        offset, for example, 2025-06-03T10:00:00+06:00. Milliseconds may be provided but are ignored. 
                                        If timeMin is set, timeMax must be greater than timeMin.

        timeZone (str):	                The timezone for the event. Defaults to "UTC".


    Returns:
        list: A list of events from the Google Calendar.
    """

    event_args_model = ListEventsParams(
        calendarId=calendarId,
        maxResults=maxResults,
        singleEvents=singleEvents,
        orderBy=orderBy,
        timeMin=timeMin,
        timeMax=timeMax,
        timeZone=timeZone
    )

    events = get_events(event_args_model)
    formatted_events = []
    for event in events:
        start = event.get("start", {})
        end = event.get("end", {})
        start_time_value = start.get("dateTime") or start.get("date")
        end_time_value = end.get("dateTime") or end.get("date")
        formatted_events.append({
            "title": event.get("summary", "Untitled"),
            "start-time": start_time_value,
            "end-time": end_time_value,
        })
    return formatted_events
