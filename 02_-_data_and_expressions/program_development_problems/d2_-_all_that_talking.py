#!/usr/bin/env python3
# All That Talking
# Develop and test a Python program that determines how much time it would take
# to download all instances of every word ever spoken. Assume the size of this
# information as given in Figure 2-1. (5EB, or 10**18)
#
# The download speed is to be entered by the user in million of bits per second
# (mbps).  To find your actual connection speed, go to the following website
# (from Intel Corporation) or similar site,
#
# www.intel.com/content/www/us/en/gamers/broadband-speed-test.html
#
# Connection speeds can vary, so run this connection speed test three times.
# Take the average of three results, and use that as the connection speed to
# enter into your program. Finally, determine what unit of time is best to
# express your results. Minutes, hours, days, other?
<<<<<<< HEAD:02_-_data_and_expressions/d2_-_all_that_talking.py

=======
"""
Input:
    * Size of a file to download
    * Approximate throughput from speedtest
    * Size of all words ever spoken, ``all_words = 10**9 # 1EB``
Processing:
    * Check if there is an internet connection by pinging 1.1.1.1
    * If so, use ``speedtest-cli`` or an api to measure the throughput of the
      connection
    * Using that measurement, compute how long it will take to download the
      file by dividing the file size by the connection speed
Output:
    * The amount of time it will take to download the file on the machines
"""
>>>>>>> 6af79f2... Spring cleaning:02_-_data_and_expressions/program_development_problems/d2_-_all_that_talking.py
file_size = float(input("File size in MB/s: "))
speed1    = float(input("Connection speed in MB/s: "))
speed2    = float(input("Connection speed in MB/s: "))
speed3    = float(input("Connection speed in MB/s: "))

print(f"The file should take {file_size / ((speed1 + speed2 + speed3) / 3)} seconds to download.")

