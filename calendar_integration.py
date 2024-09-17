from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Get credentials for Google Calendar
def get_calendar_service():
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    credentials = service_account.Credentials.from_service_account_file(
        'credentials.json', scopes=SCOPES)
    service = build('calendar', 'v3', credentials=credentials)
    return service

# Check doctor availability
def get_doctor_availability(service, calendar_id, start_time, end_time):
    events_result = service.events().list(calendarId=calendar_id,
                                          timeMin=start_time,
                                          timeMax=end_time,
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    if events:
        return [event['start']['dateTime'] for event in events]
    return None

# Book appointment
def book_appointment(service, calendar_id, patient_name, start_time, end_time):
    event = {
        'summary': f'Appointment with {patient_name}',
        'start': {
            'dateTime': start_time,
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'America/New_York',
        },
    }
    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    return f"Appointment booked: {event.get('htmlLink')}"
