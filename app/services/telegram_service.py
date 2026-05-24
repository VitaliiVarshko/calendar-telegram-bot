import requests

from app.core.config import settings
from datetime import datetime, timedelta


class TelegramService:

    def send_message(
        self,
        text
    ):

        url=(
            f"https://api.telegram.org/bot"
            f"{settings.TELEGRAM_BOT_TOKEN}"
            f"/sendMessage"
        )

        data={

            "chat_id":
                settings.TELEGRAM_CHAT_ID,

            "text":
                text
        }

        response=requests.post(
            url,
            json=data
        )

        return response.json()
    


    def create_events_message(self, events):

        today = datetime.now()

        formatted_date = today.strftime(
            "%d %B"
        )

        message = (
            f"📅 Events for today "
            f"({formatted_date}):\n\n"
        )

        if len(events) == 0:

            message += (
                "There are no events "
                "for today yet."
            )

            return message

        for index, event in enumerate(
                events,
                start=1
        ):

            start = event.get(
                "start"
            )

            summary = event.get(
                "summary"
            ) or "No title"

            description = event.get(
                "description"
            ) or ""

            event_time = datetime.fromisoformat(
                start.replace(
                    "Z",
                    "+00:00"
                )
            )

            formatted_time = (
                event_time.strftime(
                    "%H:%M"
                )
            )

            message += (
                f"{index}. {summary}\n"
                f"⏰ {formatted_time}\n"
                f"{description}\n\n"
            )

        return message