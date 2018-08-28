# As an exercise, use incremental development to write a function called hypotenuse that
# returns the length of the hypotenuse of a right triangle given the lengths of the other two
# legs as arguments. Record each stage of the development process as you go.
from math import sqrt

def hypotenuse(a, b):
    # a^2 + b^2 = c^2
    a_sqr = a**2
    b_sqr = b**2
    print(a_sqr, b_sqr)

    sum_sqrs = a_sqr + b_sqr
    print(sum_sqrs)

    c = sqrt(sum_sqrs)
    print(c)
    
    return c

print('3 & 4. Answer is 5: ', hypotenuse(3, 4))