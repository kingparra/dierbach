#!/usr/bin/env python3
# Modify the Drake’s Equation Program in section 1.7 so that it calculates
# results for a best case scenario, that is, so that factors p (percentage of
# stars that have planets), f (percentage of those planets that develop life),
# i (percentage of those planets that develop intelligent life), and c
# (percentage of those planets that can communicate with us) are all hard-coded
# as 100%. The value of R should remain as 7. Design the program so that the
# only values that the user is prompted for are how many planets per star can
# support life, n, and the estimated number of years civilizations last, L.
# **Develop a set of test cases for your program with the included test
# results**.

print("""\
Welcome to the drake equation program. This program will allow you to enter
specific values related to the likelihood of finding intelligent life in our
galaxy. All percentages should be entered as integer values, e.g., 40 and
not .40.""")

# N = R * p * n * f * i * C * L

n = int(input('How many planets per star do you think can support life?: '))
L = int(input('Number of years you think civilizations last?: '))


# Calculate result. This implemented as a function for testing with pytest.
def calculate_civs(n, L, R=7, p=100/100, f=100/100, i=100/100, C=100/100):
    return R * p * n * f * i * C * L


num_detectable_civilizations = calculate_civs(n, L)

print('Based on the values entered there are an estimated '
    f'{num_detectable_civilizations} potentially detectable '
    'civilizations in our galaxy.'
)
