# The mathematician Srinivasa Ramanujan found an infinite series that 
# can be used to generate a numerical approximation of 1/π:
#
# 1/π = (2√2)/9801 *  ∑_(k=0)^∞ (4k)!(1103+26390k)/((k!)^4 (396)^4k )
#
# Write a function called estimate_pi that uses this formula to compute and
# return an estimate of π. It should use a while loop to compute terms of 
# the summation until the last term is smaller than 1e-15 (which is Python
# notation for 10−15). You can check the result by comparing it to math.pi.

import math

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

def estimate_pi():
    k = 0
    estimate = 0
    factor = 2 * math.sqrt(2) / 9801

    while True:
        numer = fac(4*k) * (1103 + 26390 * k)
        denom = fac(k)**4 * 396 **(4*k)
        term = factor * numer / denom
        estimate += term
        
        if abs(term) < 1e-15:
            break
        
        k +=1

    return estimate**-1

print('Estimate:\t', estimate_pi())
print('math.pi:\t', math.pi)