#!/usr/bin/env python3
# This is a quick script to convert decimal numbers to binary so I don't have
# to slog through too much math to finish chapter one, exercise 11.

decimal_nums = [5, 7, 16, 15, 32, 33, 64, 63, 128, 127]

for num in decimal_nums:
    print(num, '=', format(num, 'b'))

