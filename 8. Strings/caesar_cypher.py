def rotate(string, integer):
    '''Rotate letters in string by [integer] number of places'''
    coded_str = ''

    for c in string:
        
        if c.islower():
            coded_int = ord(c) + integer
            while coded_int > 122:
                coded_int -= 26
            while coded_int < 97:
                coded_int += 26
        elif c.isupper():
            coded_int = ord(c) + integer
            while coded_int > 90:
                coded_int -= 26
            while coded_int < 65:
                coded_int += 26
        else:
            coded_int = ord(c)

        coded_str = coded_str + chr(coded_int)
        
    return coded_str

print(rotate('IBM', -1))
print(rotate('cheer', 7))
print(rotate('Melon', -10))


# -------- #
# Solution #
# -------- #

def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res