#!/usr/bin/env python3
# Losing Your Head over Chess
# The game of chess is generally believed to have been invented in India in the
# sixth century for a ruling king by one of his subjects. The king was
# supposedly very delighted with the game and asked the subject what he wanted
# in return. The subject, being clever, asked for one grain of wheat on the
# first square, two grains of wheat on the second square, four grains of wheat
# on the third square, and so forth, doubling the amount on each next square.
# The king thought that this was a modest reward for such an invention.
# However, the total amount of wheat would have been more than 1,000 times the
# current world production.  Develop and test a Python program that calculates
# how much wheat this would be in pounds, using the fact that a grain of wheat
# weighs approximately 1/7,000 of a pound.
from math import factorial

grain_weight = 1/7000 # Of a pound
squares_on_chessboard = 64
num_grains = factorial(squares_on_chessboard)

print(f"The king would have to give his subject"
      f"{num_grains * grain_weight: ,}lbs worth of wheat grains.")

