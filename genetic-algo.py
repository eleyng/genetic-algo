#---
# Implementation of GA
#---

import math

#---
# Objective Function
#---

def f(x):
    f = math.sin(x) + 0.05 * x ** 2 + 1
    return f

#---
# Code GA Script
#---

def main():

    # Code Variables
    var_prop = input('Continuous or Discrete? ')
    while var_prop != 'D' or var_prop != 'C':
        var_prop = input('Continuous or Discrete? ')
    # Discrete: find number of bits, m, needed
    if var_prop == 'D':
        num_discrete = int(input('Number of discrete values desired? '))
        m = math.log2(num_discrete)
    # Continuous: divide interval into binary representation with m bit size
    else:
        f_range = [int(x) for x in input().split()]




main()


