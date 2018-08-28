# The following functions are all intended to check whether a string 
# contains any lowercase letters, but at least some of them are wrong. 
# For each function, describe what the function actually does 
# (assuming that the parameter is a string). 

def any_lowercase1(s):
    '''Correction: Does not work as intended. Only returns case of first character.

    WRONG: Works as intended. Iterates through each character in string,
    returning true if any of them is lowercase.'''

    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    '''Does not work as intended. Iterates through characters in string
    but checks if string 'c' is lowercase, and returns 'True' as a string
    not a boolean. Will always return 'True' '''

    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    '''Does not work as intended. Will iterate through all characters in
    string, and set flag to True or False depending, however each new test
    overwrites the last and so flag only returns the state of the last 
    character in the string'''
    
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    '''Works as intended. Similar to previous, iterates through characters
    in string. If any character is lowercase, flag will be set to True.
    On the next iteration, the or logical operator will ensure flag retains
    its previous state on update, as will evaluate to True if either statement
    is True. Will remain false otherwise'''

    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    '''Does not work as intended. As soon as any letter in string isn't
    lowercase, funciton will return False and stop there'''
    for c in s:
        if not c.islower():
            return False
    return True


# Testing after explanations
string = 'MiX of UpPeR and LoWeR'

print('Will not work, returns False:', any_lowercase1(string))
print('Always returns True:', any_lowercase2(string))
print('Only last character, so False:', any_lowercase3(string))
print('Works, returns True:', any_lowercase4(string))
print('Returns False at first non-lower:', any_lowercase5(string))