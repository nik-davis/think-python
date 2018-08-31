# In-text exercises and examples

import time

count = 0


def fibonacci_slow(n):
    '''Method from earlier exercise of obtaining fibonacci number. Very slow'''
    global count
    count += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_slow(n-1) + fibonacci_slow(n-2)

known = {0:0, 1:1}

def fibonacci_memo(n):
    '''Much faster method using memoization'''
    global count
    count += 1
    if n in known:
        return known[n]
    
    res = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    known[n] = res
    return res

n = 33

print('Fast')
start_time = time.time()
print(fibonacci_memo(n))
time_taken = time.time() - start_time
print('Done in', time_taken, 'seconds, calling function', count, 'times.')

count = 0
print('Slow')
start_time = time.time()
print(fibonacci_slow(n))
time_taken = time.time() - start_time
print('Done in', time_taken, 'seconds, calling function', count, 'times.')