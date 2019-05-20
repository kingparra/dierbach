#!/usr/bin/env python3
# Write a Python program that allows the user to enter any integer value, and
# displays the value of 2 raised to that power. Your program should function as
# shown below.
#
#     What power of two? 10
#     Two to the power of 10 is 1024

exponent = int(input("What power of two? "))
result = 2 ** exponent
print(f"Two to the power of {exponent} is {result}")
