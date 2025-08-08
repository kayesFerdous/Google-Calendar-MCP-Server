## Google Calendar MCP Server

An MCP server exposing Google Calendar tools to any MCP-compatible client (e.g., Claude Desktop, Cursor MCP CLI). It lets you:

- List events in a time window
- Create events
- Delete events by summary

### Prerequisites

- Python 3.11+
- A Google Cloud project with OAuth 2.0 Client ID (Desktop) for Google Calendar API
- `credentials.json` downloaded locally (do not commit it)

### Setup

1. Clone and install dependencies

```bash
uv sync  # or: pip install -e .
```

2. Enable Google Calendar API and download OAuth credentials

- Go to Google Cloud Console → APIs & Services → Credentials
- Create OAuth client ID: Application type "Desktop app"
- Download the JSON and save it as `credentials.json` at the project root

3. First run / OAuth consent

The first call to any tool will open a browser for consent and produce `token.json` locally (ignored by git).

### Running the MCP server

```bash
python -m src.service  # Not the server entry
python main.py         # Starts the MCP over stdio
```

Use from MCP-compatible clients by pointing to `main.py` as the command.

### Tools

- get_google_calendar_events(maxResults, calendarId="primary", singleEvents=True, orderBy="startTime", timeMin=None, timeMax=None)
  - Returns a list like: [{ "title": str, "start-time": str, "end-time": str }]
- create_google_calendar_event(summary, start: datetime, end: datetime, description=None, location=None, time_zone="Asia/Dhaka")
  - Returns the created event HTML link (if available)
- delete_google_calendar_event(event_name: str)
  - Deletes the first exact summary match

### MCP client configuration (example)

Example JSON snippet for a client config:

```json
{
  "mcpServers": {
    "google-calendar": {
      "command": "python",
      "args": ["main.py"],
      "env": {}
    }
  }
}
```

### Notes

- Keep `credentials.json` and `token.json` out of git.
- Time strings must be RFC3339 with timezone (e.g., `2025-08-08T00:00:00+06:00`).
- All-day events return a `date` string instead of `dateTime`.
