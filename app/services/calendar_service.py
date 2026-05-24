from google.oauth2 import service_account
from googleapiclient.discovery import build
from app.core.config import settings
from datetime import datetime, timedelta
from app.services.telegram_service import TelegramService

class CalendarService:

    def get_today_events(self):

        # pass

        today = datetime.now()

        start_day = today.replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

        end_day = start_day + timedelta(days=1)

        credentials = service_account.Credentials.from_service_account_file(settings.GOOGLE_CREDENTIALS_FILE)

        service1 = build(
            "calendar",
            "v3",
            credentials=credentials
        )

        events1 = service1.events().list(
            calendarId=settings.GOOGLE_CALENDAR_ID,
            timeMin=start_day.isoformat() + "Z",
            timeMax=end_day.isoformat() + "Z",
            singleEvents=True,
            orderBy="startTime"
        ).execute()

        events=[]

        for event in events1["items"]:

            start=event.get("start",{}).get("dateTime")

            if start is None:

                start=event.get("start",{}).get("date")

            events.append({

                "summary":
                    event.get(
                        "summary"
                    ),

                "description":
                    event.get(
                        "description"
                    ),

                "start":
                    start
            })

        telegram=TelegramService()

        message=telegram.create_events_message(events)

        telegram.send_message(message)        

        return events
    
