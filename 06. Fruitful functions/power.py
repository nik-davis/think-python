# A number, a, is a power of b if it is divisible by b and a/b is a power of b.
# Write a function called is_power that takes parameters a and b
# and returns True if a is a power of b. 
# Note: you will have to think about the base case.

def is_power(a, b):
    if a == b:
        return True
    if a/b < b or a%b != 0:
        return False
    return is_power(a/b, b)
    
print('4, 2: ', is_power(4, 2))
print('9, 3: ', is_power(9, 3))

for i in range(20):
    print(i, is_power(i, 2))