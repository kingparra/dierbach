#!/usr/bin/env python3
# Develop and test a program that allows the user to enter an integer value
# indicating the number of cities to solve for the Traveling Salesman problem.
# The program should then output the number of years it would take to solve
# using a brute force-approach. Make use of the factorial function of the math
# module as shown in Figure 1-28. Estimate the total amount of time it takes by
# using the assumptions given in section 1.1.2.  Those assumptions, by the way,
# are that the computer can compute the lengths of one million routes per
# second.

import math

# Get the number of cities from the user.
num_cities = int(input("Enter the number of cities: "))

# Compute the number of possible routes.
possible_routes = math.factorial(num_cities)

# Calculate how many seconds it will take to compute that number of
# routes, assuming 1,000,000 routes can be computed every second.
seconds_to_compute = possible_routes / 1000000

# Convert seconds_to_compute to larger units of time.
# ...the math here is wrong.
minutes_to_compute = seconds_to_compute / 60
hours_to_compute = minutes_to_compute / 60
days_to_compute = hours_to_compute / 24
months_to_compute = days_to_compute / 30.42
years_to_compute = months_to_compute / 12

# Display the number of years it would take.
print("Years required to compute all possible routes:\t\t", years_to_compute)
