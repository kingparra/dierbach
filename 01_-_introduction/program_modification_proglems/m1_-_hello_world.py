#!/usr/bin/env python3
# Modify the sample “hello” Python program in section 1.6.5 to first request
# the user’s first name, and then request their last name. The program should
# display:
#   Hello firstname lastname
#   Welcome to Python!
# for the firstname and lastname entered.

first_name = input("Enter your first name: ")
last_name = input("Enter you last name: ")

print(f"Hello {first_name} {last_name}", "Welcome to Python!", sep="\n")
