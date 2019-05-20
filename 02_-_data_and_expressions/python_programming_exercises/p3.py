#!/usr/bin/env python3
# Write a Python program that prompts the user for two floating-point values
# and displays the result of the first number divided by the second, with
# exactly six decimal places displayed in scientific notation.

float1 = float(input("Enter the first value: "))
float2 = float(input("Enter the second value: "))

# The default precision of scientific notation 'e' in the format mini-language
# is 6 digits worth. The mini language works with printf style interpolation,
# the .format method, f-strings, and the format built-in function.
print(f"{float1} / {float2} = {float1 / float2: e}")

