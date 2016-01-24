# coding=utf-8
# Task 1.5.7
from fractions import Fraction

S1 = {1, 2, 3}
S2 = {29, 30, 4999}

S3 = {x*y for x in S1 for y in S2}

print (S3)


