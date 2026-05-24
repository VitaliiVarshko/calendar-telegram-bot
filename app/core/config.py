from dotenv import load_dotenv
import os

load_dotenv()

print("Calendar:", os.getenv("GOOGLE_CALENDAR_ID"))
print("Credentials:", os.getenv("GOOGLE_CREDENTIALS_FILE"))

class Settings:

    GOOGLE_CALENDAR_ID = os.getenv(
        "GOOGLE_CALENDAR_ID"
    )

    GOOGLE_CREDENTIALS_FILE = os.getenv(
        "GOOGLE_CREDENTIALS_FILE"
    )

    TELEGRAM_BOT_TOKEN=os.getenv(
        "TELEGRAM_BOT_TOKEN"
    )

    TELEGRAM_CHAT_ID=os.getenv(
        "TELEGRAM_CHAT_ID"
    )

settings = Settings()