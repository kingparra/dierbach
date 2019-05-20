#!/usr/bin/env python3
# Life Signs
# Develop and test a program that prompts the user for their age and determines
# approximately how many breaths and how many heartbeats the person has had in
# their life. The average respiration (breath) rate of people changes during
# different stages of development. Use the breath rates given below for use in
# your program:
#
#   Breaths per Minute
#
# ============  =========
#  Age Range     Breaths
# ============  =========
#  Infant         30–60
#  1–4 years      20–30
#  5–14 years     15–25
#  adults         12–20
# ============  =========
#
# For heart rate, use an average of 67.5 beats per second.
#
"""
input
    the users age

        age = int(input("Enter your age: "))

    the age range to breath range mappings

        age_to_breath_ranges = {
           range(0, -Inf, -1):range(30,60),
           range(1, 4):range(20, 30),
           range(5, 14):range(15, 25),
           range(15, Inf):range(12, 20)
        }

    the average heart rate of 67.5 bps

processing

output

    How many breaths and heartbeats the person has had in their life, approximately.

"""

