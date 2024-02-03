#!/usr/bin/python3.8

import datetime

def date_to_julian(year, month, day):
    date = datetime.date(year, month, day)
    return date.timetuple().tm_yday

# Prompt the user for input
input_date = input("Enter the date (format: YYYY MM DD): ")
year, month, day = map(int, input_date.split())

julian_date = date_to_julian(year, month, day)
print("Julian date:", julian_date)

