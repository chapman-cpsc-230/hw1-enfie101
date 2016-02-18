"""
File: seconds2years.py
Copyright (c) 2016 Callie Enfield
License: MIT_License
This code evaluates whether a newborn baby in Norway can expect to live for one billion seconds.  We determined anything less than 80 years is reasonable to expect.
"""
seconds = 10**9
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
years = days / 365
print (years)
if years < 80:
    print ("Yes, a newborn baby in Norway can expect to live for one billion seconds.")
else:
    print ("No, a newborn baby in Norway shouldn't expect to live for one billion seconds.")
