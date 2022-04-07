# time delta is a span of time that can assists in date and time calculations

from datetime import date, time, datetime, timedelta

def main():

    # timedelta construction
    delta = timedelta(days=365,hours=5,minutes=60)
    print(delta)

    # calculating a future date
    now = datetime.now()
    print("A year from now is:", str(now + timedelta(days=365)))

    # using multiple arguments in timedelta

    print("two weeks and 3 days from now is going to be:", str(now + timedelta(weeks=2, days=3)))

    # past time

    print("A week ago was", str(now - timedelta(weeks=1)))

    # calculate time until april fool's day

    today = date.today()
    afd = date(today.year, 4, 1)

    if afd < today:
        print("it has past by:",(today - afd).days, "days")
        afd = afd.replace(year= today.year + 1)

    print("next april fool's day is in:",(afd - today).days, "days")

if __name__ == "__main__":
    main()