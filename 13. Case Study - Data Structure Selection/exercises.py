# -------------------------------------------------------------------- #
# --------- Chapter 13. Case Study: Data Structure Selection --------- #
# -------------------------------------------------------------------- #

# 13.1. Write a program that reads a file, breaks each line into words, strips
# whitespace and punctuation from the words, and converts them to lowercase.
# Hint: The string module provides a string named whitespace, which contains 
# space, tab, newline, etc., and punctuation which contains the punctuation 
# characters.
#
#	>>> import string
#	>>> string.punctuation
#	'!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'
#	
# Also, you might consider using the string methods strip, replace and translate

import string


def open_file(filename, encoding='UTF-8'):
    '''Reads a file and returns as string.

    filename: path of file
    encoding: Optional: encoding to use (default UTF-8)

    returns: string
    '''
    return open(filename, encoding=encoding).read()
    

def get_words(filename):
    '''Returns a lower-cased list of words from a given file with
    punctuation and whitespace removed

    filename: path of file to read

    returns: list of strings
    '''
    s = open_file(filename)

    t = s.split()

    for i in range(len(t)):
        t[i] = t[i].lower()
        t[i] = t[i].strip(string.punctuation)

    return t


def ex13_1():
    '''Run ex 13.1 solution'''
    t = get_words('resources/goldenbird.txt')
    
    # Uncomment to print word list:
    # print(t)


# Run solutions
ex13_1()