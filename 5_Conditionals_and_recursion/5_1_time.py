import time
import math

def time_since_epoch():
    sec_in_m = 60
    sec_in_h = 60 * sec_in_m
    sec_in_d = 24 * sec_in_h

    origin = time.gmtime(0)
    print("Time elapsed since {} (GMT):".format(time.asctime(origin)))

    time_to_add = math.floor(time.time()) # in seconds, without the millisecs

    days = time_to_add // sec_in_d
    time_to_add %= sec_in_d # remainder after we've counted the days

    hours = time_to_add // sec_in_h
    time_to_add %= sec_in_h

    minutes = time_to_add // sec_in_m
    seconds = time_to_add % sec_in_m 

    print('{} days'.format(days))
    print('{} hours'.format(hours))
    print('{} minutes'.format(minutes))
    print('{} seconds'.format(seconds))


time_since_epoch()
