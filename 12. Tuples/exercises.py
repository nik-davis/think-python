def sumall(*args):
    '''Takes any number of arguments and returns the sum
    
    args: tuple of integers

    Returns: int'''
    total = 0
    for arg in args:
        total += arg
    return total

t = (1, 2, 3)
print(sumall(*t))
print(sumall(10))