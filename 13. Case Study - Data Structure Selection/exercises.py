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

# 13.2. Go to Project Gutenberg (http://gutenberg.org ) and download your
# favorite out-of-copyright book in plain text format.
#
# Modify your program from the previous exercise to read the book you
# downloaded, skip over the header information at the beginning of the 
# file, and process the rest of the words as before.
#
# Then modify the program to count the total number of words in the book,
# and the number of times each word is used.
#
# Print the number of different words used in the book. Compare different
# books by different authors, written in different eras. Which author uses
# the most extensive vocabulary?


def read_book(filename):
    '''Reads book from file, removing header and footer (works for poroject
    gutenberg format books)

    filename: string

    returns: string
    '''
    f = open(filename, encoding='UTF-8').readlines()
    s = str()

    write = False
    for line in f:
        if line [:7] == '*** END':
            write = False

        if write:
            s += line

        if line[:12] == '*** START OF':
            write = True

    return s

def get_words(s):
    '''Returns a lower-cased list of words from a string with
    punctuation and whitespace removed

    s: string

    returns: list of strings
    '''
    t = s.split()

    for i in range(len(t)):
        t[i] = t[i].lower()
        t[i] = t[i].strip(string.punctuation)

    return t


def count_words(t):
    '''Count number of times a word appears in a list, storing as values
    in a dictionary.

    t: list

    returns: dict of word:frequency
    '''
    d = dict()
    for word in t:
        d[word] = d.get(word, 0)
        d[word] += 1
    return d


def count_book(bookname, filename):
    '''Count and print total number of words, and number of different words
    in a given book, supplied in txt format
    
    bookname: string
    filename: string

    returns: None
    '''
    s = read_book(filename)
    t = get_words(s)

    d = count_words(t)

    total_words = len(t)
    words_used = len(d)

    print('Total number of words in {0}: {1}'.format(bookname, total_words))
    print('Number of different words used:', words_used)
    print()

def ex13_2():
    '''Run ex 13.2 solution'''

    count_book('Grimm', 'resources/grimm.txt')
    count_book('Beowulf', 'resources/beowulf.txt')
    count_book('Frankenstein', 'resources/frankenstein.txt')


# Run solutions
# ex13_1()
ex13_2()

