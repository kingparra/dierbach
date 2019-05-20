#!/usr/bin/env python3
# Your Place in the Universe Program

# This program will determine the approximate number of atoms that a
# person consists of and the percent of the universe that they comprise.

# intialization
num_atoms_universe = 10e80
weight_avg_person = 70 # 70 kg (145 lbs)
num_atoms_avg_person = 7e27

# program greeting
print('This program will determine your place in the universe.')

# prompt for user's weight
weight_lbs = int(input('Enter your weight in pounds: '))

# convert weight to kilograms
weight_kg = 2.2 * weight_lbs

# determine number atoms in person
num_atoms = (weight_kg / 70) * num_atoms_avg_person
percent_of_universe = (num_atoms / num_atoms_universe) * 100

# display results
print('You contain approximately', format(num_atoms, '.2e'), 'atoms')
print('Therefore, you comprise', format(percent_of_universe, '.2e'),
      '% of the universe')

