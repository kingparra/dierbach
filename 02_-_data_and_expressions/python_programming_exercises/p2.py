#!/usr/bin/env python3
# Write a Python program that prompts the user for two floating-point values
# and displays the result of the first number divided by the second, with
# exactly six decimal places displayed.
float1 = float(input("Enter the first value: "))
float2 = float(input("Enter the second value: "))
print(f"{float1} / {float2} = {float1 / float2: .6f}")

