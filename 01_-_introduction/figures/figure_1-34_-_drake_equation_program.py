# *************************************
#  Figure 1-34: Drake Equation Program
# *************************************
#
# SETI Program
#
# The Drake equation, developed by Frank Drake in the 1960s, attempts to
# estimate how many extraterrestrial civilizations, N, may exist in our
# galaxy at any given time that we might come in contact with,
#
#   N = R * p * n * f * i * c * L
#
# where,
#
#   R ... estimated rate of star creation in our galaxy
#   p ... estimated percent of stars that have planets
#   n ... estimated average number of planets that can potentially support
#         life for each star with planets
#   f ... estimated percent of those planets that actually go on to develop life
#   i ... estimated percent of those planets go on to develop intelligent life
#   c ... estimated percent of those that are willing and able to communicate
#   L ... estimated expected lifetime of such civilizations
#
# Given the value for R, 7 per year, is the least disputed of the values, the
# user will be prompted to enter estimated values for the remaining six
# factors. The estimated number of civilizations that may be detected in our
# galaxy will then be displayed.

# display program welcome
print('Welcome to the SETI program')
print('This program will allow you to enter specific values related to')
print('the likelihood of finding intelligent life in our galaxy. All')
print('percentages should be entered as integer values, e.g., 40 and not .40')
print()

# get user input
p = int(input('What percentage of stars do you think have planets?: '))
n = int(input('How many places per star do you think can support life?: '))
f = int(input('What percentage do you think actually develop life?: '))
i = int(input('What percentage of those do you think have intelligent life?: '))
c = int(input('What percentage of those do you think can communicate with us?: '))
L = int(input('Number of years you think civilizations last?: '))

# calculate result
num_detectable_civilizations = 7 * (p/100) * n * (f/100) * (i/100) * (c/100) * L

# display result
print()
print('Based on the values entered ...')
print('there are an estimated', round(num_detectable_civilizations),
      'potentially detectable civilizations in our galaxy')

