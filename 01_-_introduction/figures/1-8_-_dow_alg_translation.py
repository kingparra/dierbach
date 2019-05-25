#!/usr/bin/env python3
import math


def isLeapYear(year):
    if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
        return True


def dow(year, month, day):
    century_digits = year // 100
    year_digits = year % 100
    value = year_digits + math.floor(year_digits / 4)

    if century_digits == 18:
        value += 2
    elif century_digits == 20:
        value += 6
    elif (month == "Feburary") and (isLeapYear(year) is True):
        value += 4
    elif month == "March" or month == "November":
        value += 4
    elif month == "May":
        value += 2
    elif month == "June":
        value += 5
    elif month == "August":
        value += 3
    elif month == "October":
        value += 1
    elif month == "September" or month == "December":
        value += 6

    value = (value + day) % 7

    if value == 1:
        return "Sunday"
    elif value == 2:
        return "Monday"
    elif value == 3:
        return "Tuesday"
    elif value == 4:
        return "Wednesday"
    elif value == 5:
        return "Thursday"
    elif value == 6:
        return "Friday"
    elif value == 0:
        return "Saturday"


def main():
    year = int(input("Year: "))
    month = input("Month: ")
    day = int(input("Day: "))
    dow(year, month, day)


if __name__ == '__main__':
    main()

