
def check_fermat(a, b, c, n):
    '''Takes values for a, b, c and n to test Fermat's last theorem
    '''
    if a**n + b**n == c**n and n > 2:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')
    
def fermat_prompt():
    '''Prompts the user for input values a, b, c, and n to test Fermat's last theorem
    '''
    a = int(input('Input value for a: '))
    b = int(input('Input value for b: '))
    c = int(input('Input value for c: '))
    n = int(input('Input value for n: '))

    check_fermat(a, b, c, n)

fermat_prompt()
