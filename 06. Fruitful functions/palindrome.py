def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(word):
    '''Returns True if word is a palindrome.'''
    if len(word) <= 1:
        return True
    elif first(word) == last(word):
        return is_palindrome(middle(word))
    return False

def is_palindrome_alt(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print('No: ', is_palindrome('no'))
print('non: ', is_palindrome('non'))

print('allen: ', is_palindrome('allen'))
print('bob: ', is_palindrome('bob'))
print('otto: ', is_palindrome('otto'))
print('redivider: ', is_palindrome('redivider'))
print('<blank>: ', is_palindrome(''))