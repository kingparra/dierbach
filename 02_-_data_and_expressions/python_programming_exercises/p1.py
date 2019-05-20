#!/usr/bin/env python3
# Write a Python program that prompts the user for two integer values and
# displays the result of the first number divided by the second, with exactly
# two decimal places displayed.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"{num1} / {num2} = {num1 / num2: .2f}")
