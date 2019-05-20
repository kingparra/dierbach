#!/usr/bin/env python3
# Write a Python program that allows the user to enter two integer values, and
# displays the results when each of the following arithemetic operators are
# applied. For example, if the user enters the values 7 and 5, the output would
# be:
#
#   7 + 5 = 12
#   7 - 5 = 2
#   7 * 5 = 35
#   7 / 5 = 1.40
#   7 // 5 = 1
#   7 % 5 = 2
#   7 ** 5 = 16,807
#
# All floating-point results should be displayed with two decimal places of
# accuracy. In addition, all values should be displayed with commas where
# appropriate.
#
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operators = ['+', '-', '*', '/', '//', '%', '**']
for operator in operators:
    print(f"{num1} {operator} {num2} =", eval(f"{num1} {operator} {num2}"))
