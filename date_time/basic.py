# working with datetime

from datetime import date
from datetime import time
from datetime import datetime

def main():
    # get today's date
    today = date.today()
    print("today's date is:", today)

    # get indivual month, year and day
    print("date is:", today.month, today.year, today.day)

    # current date and time
    weekdays = datetime.now()
    print(weekdays)

    # weekdays numbers
    days = ["Mon","Tue","Wed","Thurs","Fri","Sat","Sun"]
    print("today is day number:",weekdays.weekday(),"according to python weekday count")
    print("So it's:", days[weekdays.weekday()])

    # current time
    t = datetime.time(weekdays)
    print(t)


if __name__ == "__main__":
    main()