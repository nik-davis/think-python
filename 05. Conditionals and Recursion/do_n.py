def print_hi():
    print('hi')

def do_n(f, n):
    if n <= 0:
        return
    else:
        f()
        do_n(f, n-1)

do_n(print_hi, 2)
