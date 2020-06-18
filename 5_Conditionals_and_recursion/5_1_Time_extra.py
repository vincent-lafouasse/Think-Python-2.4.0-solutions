import time
import math

# https://docs.python.org/3/library/time.html
# The epoch is the point where the time starts, and is platform dependent. 
# For Unix, the epoch is January 1, 1970, 00:00:00 (UTC).
# To find out what the epoch is on a given platform, look at time.gmtime(0).

def to_add():
    to_add = math.floor(time.time()) # i don't care for milliseconds

    days = to_add // (24*3600)
    to_add %= 24*3600

    hours = to_add // 3600
    to_add %= 3600

    minutes = to_add // 60
    seconds = to_add % 60

    return (days, hours, minutes, seconds)

def is_leap(year):
    return (year%4 == 0 and year%100 !=0) or year%400 == 0

def year_len(year):
    return 366 if is_leap(year) else 365

def add_year(year, days):

    while days >= year_len(year):
        days -= year_len(year)
        year += 1

    return (year, days)


def month_len(month, year):
    long_months = (1, 3, 5, 7, 8, 10, 12) 
    short_months = (4, 6, 9, 11)

    if month in long_months:
        return 31
    elif month in short_months:
        return 30
    elif is_leap(year):
        return 29
    else:
        return 28

def add_month(month, days, year):

    while days >= month_len(month, year):
        days -= month_len(month, year)
        month += 1

    return(month, days)

def date():

    year = 1970
    month = 1
    day = 1

    days_to_add, hours, minutes, seconds = to_add()

    year, days_to_add = add_year(year, days_to_add)

    month, day = add_month(month, days_to_add, year)

    return (year, month, day, hours, minutes, seconds)

print(date())
