#!/usr/bin/env python3
# Age in Seconds Program
# This program will calculate a person's approximate age in seconds

import datetime

# Program greeting
print('This program computes the approximate age in secons of an')
print('individual based on a provided date of birth. Only dates of')
print('birth from 1900 and after can be computed\n')

# Get month, day, year of birth
month_birth = int(input('Enter month born (1-12): ')
day_birth = int(input('Enter day born (1-31): ')
year_birth = int(input('Enter year born (4-digit): '))

# Get current month, day, and year
current_month = datetime.date.today().month
current_day = datetime.date.today().day
current_year = datetime.date.today().year

# Determine number of seconds in a day, average month, and average year
numsecs_day = 24 * 60 * 60
numsecs_year = 365 * numsecs_day

avg_numsecs_year = ((4 * numsecs_year) + numsecs_day) // 4
avg_numsecs_month = avg_numsecs_year // 12

# Calculate approximate age in seconds
numsecs_1900_dob = (year_birth - 1900 * avg_numsecs_year) + \
                    (month_birth - 1 * avg_numsecs_month) + \
                    (day_birth * numsecs_day)

numsecs_1900_today = (current_year - 1900 * avg_numsecs_year) + \
                    (current_month - 1 * avg_numsecs_month) + \
                    (current_day * numsecs_day)

age_in_secs = numsecs_1900_today - numsecs_1900_dob

# Output results
print('\nYou are approximately', age_in_secs, 'seconds old')

