from app.services.calendar_service import CalendarService
import sys

def main():
    print("The calendar has been launched")
    

    CalendarService().get_today_events()

        

if __name__ == "__main__":
    sys.exit(main())