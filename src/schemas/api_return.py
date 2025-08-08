from pydantic import BaseModel


class CalendarListItem(BaseModel):
    title: str
    time: str
