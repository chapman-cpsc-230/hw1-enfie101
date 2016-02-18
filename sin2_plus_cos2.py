"""
File: sin2_plus_cos2.py
Copyright: (c) 2016 Callie Enfield
License: MIT_License
This code verified mathematic equations and also solved for a value using different variables and equations.
"""
import math
from math import sin, cos, pi
x = pi / 4
value = math.sin(x)**2 + math.cos(x)**2
print value


v0 = 3 #m/s
t = 1 #s
a = 2**2 #2 m/s squared
s = v0*t + 0.5*a*t**2
print s


a = 3
b = 5
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2*a*b + b2
eq1_pow = (a + b)**2
print eq1_sum == eq1_pow

a = 3
b = 3
a2 = a**2
b2 = b**2
eq2_sum = a2 - 2*a*b + b2
eq2_pow = (a - b)**2
print eq2_sum == eq2_pow
