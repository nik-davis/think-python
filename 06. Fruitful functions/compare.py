# Write a compare function takes two values, x and y, 
# and returns 1 if x > y, 0 if x == y, and -1 if x < y

def compare(x, y):
    '''Takes two values, x and y, and returns 1 if x is bigger, -1 if x
    is smaller, and 0 if they are equal.'''

    if x > y:
        value = 1
    if x == y:
        value = 0
    if x < y:
        value = -1

    return value

a = compare(1, 1)
b = compare(1, 0)
c = compare(0, 1)

print('Equal: \t\t ', a)
print('x is bigger: \t ', b)
print('x is smaller: \t', c)
