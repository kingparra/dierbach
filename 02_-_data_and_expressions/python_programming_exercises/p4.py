#!/usr/bin/env python3
# Write a Python program that prompts the user to enter an upper or lower case
# letter and displays the corresponding Unicode encoding.
letter = input("Enter a letter: ")
print("The unicode codepoint for that letter is: ", ord(letter))
