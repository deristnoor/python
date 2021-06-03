# 12
# Buatlah fungsi rajut
# print(rajut('CCoCodCode'))
# print(rajut('PPyPytPythPythoPython'))
# print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
# Output:
# Code
# Python
# Purwadhika

import math

def rajut(word):    
    a = 1
    b = 1
    c = len(word) * 2
    n = int((-b + math.sqrt(b ** 2 - 4 * a * -c)) / 2 * a)
    print(word[-n:])
    return

x = 'PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'
rajut(x)