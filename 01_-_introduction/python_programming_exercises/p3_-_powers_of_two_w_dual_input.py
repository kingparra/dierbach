#!/usr/bin/env python3
# Write a Python program that allows the user to enter any integer base and
# integer exponent, and displays the value of the base raised to that exponent.
# Your program should function as shown below.
#     What base? 10
#     What power of 10 ? 4
#     10 to the power of 4 is 10000

base = int(input("What base? "))
exponent = int(input(f"What power of {base}? "))
print(f"{base} to the power of {exponent} is {base ** exponent}.")

