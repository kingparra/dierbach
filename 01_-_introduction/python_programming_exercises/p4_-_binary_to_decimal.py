#!/usr/bin/env python3
# Write a Python program that allows the user to enter a four-digit binary
# number and displays its value in base 10. Each binary digit should be entered
# one per line, starting with the leftmost digit , as shown below.
#
# Enter leftmost digit: 1
# Enter the next digit: 0
# Enter the next digit: 0
# Enter the next digit: 1
# The value is 9
#
# Since it seems tedious to type in the digits that way let's allow the user to
# type all digits at once.

print("This program converts a four digit binary number to decimal.")
binary_str = input("Enter the four digit binary number: ")
while set(binary_str) != set('01') or len(binary_str) != 4:
    binary_str = input("Bad input, enter a four digit binary number: ")
    try:
        binary_int = int(binary_str, base=2)
    except ValueError:
        print(f"Couldn't convert {binary_str} to integer.")
print(f"The value is {binary_int}")

