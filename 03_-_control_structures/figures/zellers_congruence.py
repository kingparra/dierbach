#!/usr/bin/env python3
# python3 program to find find the day for a date
# this code is contributed by nikita tiwari
# Taken from https://www.geeksforgeeks.org/zellers-congruence-find-day-date/

def zellers_congruence(day, month, year):
    day_names = {
        0:"Saturday",
        1:"Sunday",
        2:"Monday",
        3:"Tuesday",
        4:"Wednesday",
        5:"Thursday",
        6:"Friday",
        }

    if month == 1:
        month = 13
        year = year - 1

    if month == 2:
        month = 14
        year = year - 1

    q = day
    m = month
    k = year % 100
    j = year // 100 # Year digits (last two digits of year)
    h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    h = h % 7

    return day_names.get(h)


# Driver code
zellers_congruence(22, 10, 2017)

