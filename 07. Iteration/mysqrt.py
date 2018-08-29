# Copy the loop from Section 7.5 and encapsulate it in a function called
# mysqrt that takes a as a parameter, chooses a reasonable value of x,
# and returns an estimate of the square root of a. 
# 
# To test it, write a function named test_square_root that prints a table
# 
# The first column is a number, a; the second column is the square root 
# of a computed with mysqrt; the third column is the square root computed 
# by math.sqrt; the fourth column is the absolute value of the difference 
# between the two estimates.

import math

def mysqrt(a):
    epsilon = 0.00000000000001
    x = a

    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    
    return x

def test_square_root():
    print('a \tmysqrt(a) \tmath.sqrt(a) \tdiff')
    print('- \t--------- \t------------ \t----')
    for a in range(1, 10):
        my_sqrt = float(mysqrt(a))
        math_sqrt = math.sqrt(a)
        diff = abs(my_sqrt - math_sqrt)

        my_sqrt_str = str(round(my_sqrt, 11))
        math_sqrt_str = str(round(math_sqrt, 11))
        diff_str = str(diff)

        if len(my_sqrt_str) < 10:
            output = '{0}\t{1}\t\t{2}\t\t{3}'.format(a, my_sqrt_str, math_sqrt_str,
            diff_str)
        else:
            output = '{0}\t{1}\t{2}\t{3}'.format(a, my_sqrt_str, math_sqrt_str,
            diff_str)
        print(output)
        
print('\n')
test_square_root()
print('\n')