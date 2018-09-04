# 12.4 Variable-Length Argument Tuples

def sumall(*args):
    '''Takes any number of arguments and returns the sum
    
    args: tuple of integers

    Returns: int'''
    total = 0
    for arg in args:
        total += arg
    return total

t = (1, 2, 3)
print('sumall  t:', sumall(*t))
print('sumall 10:', sumall(10))

# 12.5 Lists and Tuples

s = 'abc'
t = (1, 2, 3)
zipped_list = list(zip(s,t))
print('zipped_list:', zipped_list)

for letter, number in zipped_list:
    print('tuple assignment:', number, letter)

def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False


t1 = 'abc'
t2 = (1, 'b', 2)
print('has_match:', has_match(t1, t2))

for index, element in enumerate('abc'):
    print('enumerate:', index, element)


# 12.6 Dictionaries and Tuples

d =  {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)


for key, value in d.items():
    print(key, value)


t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)
print(d)


d = dict(zip('abc', range(3)))
print(d)