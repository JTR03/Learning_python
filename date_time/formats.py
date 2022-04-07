# formatting of dates and times

from datetime import datetime

def main():
    now = datetime.now()

    # using the strftime function

    print(now.strftime("current year is: %Y"))
    print(now.strftime("today is %a %d %B %y"))

    # using local time and date format

    print(now.strftime("Local time and dates: %c"))
    print(now.strftime("local date: %x"))
    print(now.strftime("Local time: %X"))

    # formatting time

    print(now.strftime("Current time is: %I:%M:%S:%p"))
    print(now.strftime("24-hour format: %I:%M"))
    
if __name__ == "__main__":
    main()