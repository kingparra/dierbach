#!/usr/bin/env python3
# Write a simple Python program that prompts the user for a certain number of
# cities for the Traveling Salesman problem, and displays the total number of
# possible routes that can be taken. Your program should function as shown
# below.
# How many cities? 10
# For 10 cities, there are 3628800 possible routes
from math import factorial
num_cities = int(input("How many cities? "))
num_routes = factorial(num_cities)
print(f"For {num_cities} cities, there are {num_routes} possible routes.")
