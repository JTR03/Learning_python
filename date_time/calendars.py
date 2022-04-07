# working with calendars

import calendar

def main():
    c = calendar.TextCalendar(calendar.SUNDAY)
    f = c.formatmonth(2022,1,0,0)
    print(f)

    # HTML celendar format
    # hc = calendar.HTMLCalendar(calendar.SUNDAY)
    # hf = hc.formatmonth(2022,1)
    # print(hf)

    # looping over days of the month
    for i in c.itermonthdays(2022, 3):
        print(i)

    # get local names of days and months
    for name in calendar.month_name:
        print(name)

    for days in calendar.day_name:
        print(days)

    # first friday of each month
    print("First Friday of each month is on: ")

    for m in range(1,13):
        cal = calendar.monthcalendar(2022,m)
        weekone = cal[0]
        weektwo = cal[1]

        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]
        
        print(calendar.month_name[m], meetday)

if __name__ == '__main__':
    main()