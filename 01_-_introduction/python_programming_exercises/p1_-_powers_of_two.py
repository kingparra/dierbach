#!/usr/bin/env python3
# Write a simple Python program that displays the following powers of 2, one
# per line: 2**1 , 2**2 , 2**3 , 2**4 , 2**5 , 2**6 , 2**7 , 2**8.

print(*[2 ** num for num in range(1, 8)], sep='\n')

