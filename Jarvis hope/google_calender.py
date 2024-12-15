from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import datetime
import pickle

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
    creds = None
    # Load saved credentials
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If credentials are not available or invalid, authenticate user
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('calendar', 'v3', credentials=creds)

def list_events():
    service = authenticate_google_calendar()
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Fetching upcoming events...')
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"{start}: {event['summary']}")

def add_event(summary, date, time):
    service = authenticate_google_calendar()
    event = {
        'summary': summary,
        'start': {'dateTime': f'{date}T{time}:00', 'timeZone': 'UTC'},
        'end': {'dateTime': f'{date}T{time}:30', 'timeZone': 'UTC'},
    }
    service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event '{summary}' added successfully!")
