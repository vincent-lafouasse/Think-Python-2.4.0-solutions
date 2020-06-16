import time
import math

# a year has 365 days in general, and 366 days if it's a leap year

def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


time = time.time()

s_in_min = 60
s_in_h = 3600
s_in_day = 24 * 3600

year = 1970
month = 1
day = 1
hour = 0
minute = 0
second = 0
millisec = 0

while (is_leap(year) and time >= 366*s_in_day) or (not is_leap(year) and time >= 365*s_in_day):
    year += 1
    num_days = 366 if is_leap(year) else 365
    time -= num_days * s_in_day

long_months = (1, 3, 5, 7, 8, 10, 12)
short_months = (4, 6, 9, 11)

while (month in long_months and time >= 31*s_in_day) or (month in short_months and time >= 30 * s_in_day) or (is_leap(year) and time >= 29 * s_in_day) or ( time >= 28 * s_in_day):
   
    if month in long_months:
        num_days = 31
    elif month in short_months:
        num_days = 30
    elif is_leap(year):
        num_days = 29
    else:
        num_days = 28

    month += 1
    time -= num_days * s_in_day


day += time // s_in_day

time = time % s_in_day

hour += time // s_in_h

time = time % s_in_h

minute += time // s_in_min

time = time % s_in_min

second += math.floor(time)

millisec = 1000 * (time - math.floor(time))

subdivisions = (year, month, day, hour, minute, second, millisec)

for divi in subdivisions:
    print(divi)
