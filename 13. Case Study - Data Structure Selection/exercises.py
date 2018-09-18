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


def get_words(filename, skiphead=True):
    '''Returns a lower-cased list of words from a given file with
    punctuation and whitespace removed

    filename: path of file to read

    returns: list of strings
    '''
    fin = open(filename, encoding='UTF-8')

    word_list = []
    punctuation = string.punctuation + '‘’“”'
    whitespace = string.whitespace
    
    # Skip gutenberg hearder
    if skiphead == True:
        for line in fin:
            if line.startswith('*** START'):
                break
    
    for line in fin:
        # Once reach gutenberg footer, stop
        if line.startswith('*** END'):
            break
        
        line = line.replace('-', ' ')

        for word in line.split():
            word = word.strip(punctuation + whitespace).lower()
            word_list.append(word)

    return word_list


def ex13_1():
    '''Run ex 13.1 solution'''
    t = get_words('resources/goldenbird.txt', skiphead=False)
    
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


def histogram(t):
    '''Create a histrogram from iterable

    t: iterable

    returns: dict of value:frequency
    '''
    d = dict()
    for item in t:
        d[item] = d.get(item, 0)
        d[item] += 1
    return d


def count_book(filename, bookname='Unknown Title'):
    '''Count and print total number of words, and number of different words
    in a given book, supplied in txt format
    
    bookname: string
    filename: string

    returns: dict of word:frequency
    '''
    t = get_words(filename)
    hist = histogram(t)

    total_words = len(t)
    words_used = len(hist)

    print('Total number of words in {0}: {1}'.format(bookname, total_words))
    print('Number of different words used:', words_used)
    print()

    return hist


def ex13_2():
    '''Run ex 13.2 solution'''
    
    global grimm
    grimm = count_book('resources/grimm.txt', 'Grimm')
    beowulf = count_book('resources/beowulf.txt', 'Beowulf')
    frankenstein = count_book('resources/frankenstein.txt', 'Frankenstein')


# 13.3. Modify the program from the previous exercise to print the 20 most 
# frequently used words in the book. 


def invert_dict(d):
    '''Invert a dictionary, mapping old keys to a list of values where 
    new keys are the old values.

    d: dict of key:value

    returns: dict of value:key
    '''
    inverse = dict()
    for key in d:
        inverse.setdefault(d[key], []).append(key)
    return inverse

def ex13_3():
    '''Run solution to ex 13.3.'''
    # Invert grimm histogram
    inverted_dict = invert_dict(grimm)
    # Retrieve sorted list of keys, i.e. most to least frequent indices
    sorted_inverted_list = sorted(invert_dict(grimm), reverse=True)
    
    # Using the top twenty frequencies (also indices), print out the word
    for key in sorted_inverted_list[:20]:
        print('{0}: {1}'.format(key, inverted_dict[key]))


# 13.4. Modify the previous program to read a word list (see Section 9.1) 
# and then print all the words in the book that are not in the word list. 
# How many of them are typos? How many of them are common words that should
# be in the word list, and how many of them are really obscure?


def build_word_list():
    '''Builds word list from text file

    returns: list of strings
    '''
    fin = open('resources/words.txt')
    word_list = []

    for line in fin:
        word = line.strip()
        word_list.append(word)

    return word_list


def ex13_4():
    
    word_list = build_word_list()

    # For words in book, add to list if not in word list
    not_in_list = []
    for key in grimm:
        if key not in word_list:
            not_in_list.append(key)
    
    # Categorise words; many are hyphenated or have apostrophe, so can be
    # seperated out. The rest are most likely missing from the list, obscure
    # or something else (such as a name or number).
    hyphenated = []
    apostrophe = []
    rest = []

    for word in not_in_list:
        if '-' in word:
            hyphenated.append(word)
        elif '’' in word:
            apostrophe.append(word)
        else:
            rest.append(word)

    print('Hyphenated words:', len(hyphenated))
    print('Words with apostrophe:', len(apostrophe))
    print('Rest of words:', len(rest))
    print(rest)

    
# 13.5.  Write a function named choose_from_hist that takes a histogram 
# as defined in Section 11.2 and returns a random value from the histogram, 
# chosen with probability in proportion to frequency. 
# 
# For example, for this histogram:
#
#	>>> t = ['a', 'a', 'b']
#	>>> hist = histogram(t)
#	>>> hist
#	{'a': 2, 'b': 1}
#	
# your function should return 'a' with probability 2/3 and 'b' with probability 1/3.


import random


def choose_from_hist(d):
    '''Returns a random value from a histogram, chosen with probability
    in proportion to frequency.

    d: dict of value:frequency

    returns: value
    '''
    t = list()
    for key in d:
        for i in range(d[key]):
            t.append(key)
    
    # Same result using items method and extend
    t = []
    for word, freq in d.items():
        t.extend([word] * freq)
    
    return random.choice(t)

def ex13_5():
    t = ['a', 'a', 'b']
    hist = histogram(t)
    print(hist)
    for i in range(5):
        value = choose_from_hist(hist)
        print(value)


# 13.6. Python provides a data structure called set that provides many 
# common set operations. Write a program that uses set subtraction to find
# words in the book that are not in the word list.


def subtract(d1, d2):
    '''Subtraction using sets. Returns set of keys that appear in d1 but not d2.

    d1, d2: dictionaries

    returns: set
    '''
    return set(d1) - set(d2)


def ex13_6():
    d1 = {'a': 0, 'b': 0}
    d2 = {'b': 0, 'c': 0}
    print(subtract(d1, d2))


# 13.7. Write a program that uses this algorithm to choose a random word from the book. 
#	1. Use keys to get a list of the words in the book.
#	2. Build a list that contains the cumulative sum of the word frequencies
#       (see Exercise 10.2). The last item in this list is the total number
#       of words in the book, n.
#	3. Choose a random number from 1 to n. Use a bisection search 
#       (See Exercise 10.10) to find the index where the random number would
#       be inserted in the cumulative sum.
#   4. Use the index to find the corresponding word in the word list.


# Run solutions
# ex13_1()
# ex13_2()
# ex13_3()
# ex13_4()
# ex13_5()
# ex13_6()