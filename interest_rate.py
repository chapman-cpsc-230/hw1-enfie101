"""
File: interest_rate.py
Copyright: (c) 2016 Callie Enfield
License: MIT_License
This code determines the amount of Euros a given amount would grow to after a given amount of time with a fixed interest rate.
"""
A = 1000
n = 3
p = 0.05
amount = A * (1 + p / 100) ** n
print (amount)
