from mcp.server.fastmcp import FastMCP
from src.tools.create_event_tool import create_google_calendar_event
from src.tools.get_events_tool import get_google_calendar_events
from src.tools.delete_event_tool import delete_google_calendar_event


mcp = FastMCP(name="Simple Calendar MCP")

mcp.tool()(get_google_calendar_events)
mcp.tool()(create_google_calendar_event)
mcp.tool()(delete_google_calendar_event)

if __name__ == "__main__":
    mcp.run(transport="stdio")
