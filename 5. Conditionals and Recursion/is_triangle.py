def is_triangle(a, b, c):
    '''Takes three parameters a, b and c, and tests if it is possible to
    form a triangle with these lengths
    '''
    if a > b + c or b > a + c or c > a + b:
        return False
    else:
        return True

def prompt_user():
    '''
    '''
    a = int(input('Input three sticks lengths.\nStick 1: '))
    b = int(input('Stick 2: '))
    c = int(input('Stick 3: '))

    if is_triangle(a, b, c) == True:
        print('You can form a triangle with lengths {0}, {1} and {2}.'
        .format(a, b, c))
    else:
        print('Sorry, that triangle is impossible.')


prompt_user()