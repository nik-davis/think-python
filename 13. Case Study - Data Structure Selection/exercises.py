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


def get_words(filename, skiphead=True, numskip=False, allow_punc=False, lower=True):
    '''Returns a lower-cased list of words from a given file with
    punctuation and whitespace removed

    filename: path of file to read

    returns: list of strings
    '''
    fin = open(filename, encoding='UTF-8')

    word_list = []

    punctuation = string.punctuation + '‘’“”'
    whitespace = string.whitespace

    if allow_punc:
        skippables = whitespace
    else:
        skippables = punctuation + whitespace

    numbers = '1234567890'
    if numskip:
        skippables += numbers

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
            word = word.strip(skippables)
            if lower:
                word = word.lower()
            if word != '':
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


def count_book(filename, bookname='Unknown Title', output=False, numskip=False):
    '''Count and print total number of words, and number of different words
    in a given book, supplied in txt format

    bookname: string
    filename: string

    returns: dict of word:frequency
    '''
    t = get_words(filename, numskip=numskip)
    hist = histogram(t)

    total_words = len(t)
    words_used = len(hist)

    if output:
        print('Total number of words in {0}: {1}'.format(
            bookname, total_words))
        print('Number of different words used:', words_used)
        print()

    return hist


def ex13_2():
    '''Run ex 13.2 solution'''
    grimm = count_book('resources/grimm.txt', 'Grimm', output=True)
    beowulf = count_book('resources/beowulf.txt',
                         'Beowulf', output=True, numskip=True)
    frankenstein = count_book(
        'resources/frankenstein.txt', 'Frankenstein', output=True)


# 13.3. Modify the program from the previous exercise to print the 20 most
# frequently used words in the book.


def most_common(hist):
    '''Return a list of words in descending order of frequency.

    hist: map from word to frequency

    returns: list of (freq, word) pairs
    '''
    t = []

    for word, freq in hist.items():
        t.append((freq, word))

    t.sort(reverse=True)
    return t


def ex13_3():
    '''Run solution to ex 13.3.'''
    book = count_book('resources/grimm.txt', 'Grimm')

    # Get sorted list of freq-word pairs
    t = most_common(book)

    print('Most frequent words in Grimm:')
    for freq, word in t[:20]:
        gap = ' ' * (15 - len(word))
        print(' {0}:{1}{2}'.format(word, gap, freq))


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
    book = count_book('resources/grimm.txt', 'Grimm')
    word_list = build_word_list()

    not_in_list = []
    for word in book:
        if word not in word_list:
            not_in_list.append(word)

    print('Words not in list:', len(not_in_list))
    print(not_in_list)


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

    d1, d2: iterables

    returns: set
    '''
    return set(d1) - set(d2)


def ex13_6():
    d1 = {'a': 0, 'b': 0}
    d2 = {'b': 0, 'c': 0}
    print('Set subtraction:', d1, '-', d2, '=', subtract(d1, d2))

    book = count_book('resources/grimm.txt')
    word_list = build_word_list()

    not_in_list = subtract(book, word_list)
    print('Words from grimm not in word list:', len(not_in_list))
    print(not_in_list)


# 13.7. Write a program that uses this algorithm to choose a random word from the book.
#	1. Use keys to get a list of the words in the book.
#	2. Build a list that contains the cumulative sum of the word frequencies
#       (see Exercise 10.2). The last item in this list is the total number
#       of words in the book, n.
#	3. Choose a random number from 1 to n. Use a bisection search
#       (See Exercise 10.10) to find the index where the random number would
#       be inserted in the cumulative sum.
#   4. Use the index to find the corresponding word in the word list.

from bisect import bisect


def setup(hist):
    '''Builds required variables for using rand_word.

    filename: path

    returns: tuple of (list of strings, list of ints, int)
    '''
    words = []
    freqs = []
    total = 0

    for word, freq in hist.items():
        words.append(word)
        total += freq
        freqs.append(total)

    return words, freqs, total


def rand_word(words, freqs, total):
    '''Returns a word picked at random from a book.

    words: list of strings
    freqs: list of ints
    total: int

    returns: string
    '''
    n = random.randint(0, total-1)
    index = bisect(freqs, n)
    return words[index]


def ex13_7():
    filename = 'resources/grimm.txt'
    hist = histogram(get_words(filename))
    words, freqs, total = setup(hist)

    print('Random words from Grimm:')
    for i in range(50):
        word = rand_word(words, freqs, total)
        print(word, end=' ')


# 13.8. Markov analysis:
#
# 1. Write a program to read a text from a file and perform Markov analysis.
#    The result should be a dictionary that maps from prefixes to a collection
#    of possible suffixes. The collection might be a list, tuple, or dictionary;
#    it is up to you to make an appropriate choice. You can test your program
#    with prefix length two, but you should write the program in a way that
#    makes it easy to try other lengths.
#
# 2. Add a function to the previous program to generate random text based
#    on the Markov analysis.
#
#  	 What happens if you increase the prefix length? Does the random text
#    make more sense?
#
# 3. Once your program is working, you might want to try a mash-up:
#    if you combine text from two or more books, the random text you generate
#    will blend the vocabulary and phrases from the sources in interesting ways


def perform_markov(words, n):
    '''Markov Analysis: Generate a mapping of prefixes to suffixes.

    words: list of str
    n: int, length of prefix

    returns: dict mapping prefix to suffixes
    '''
    prefixes = dict()

    for i in range(len(words) - n):
        prefix = tuple()
        for j in range(i, i+n):
            prefix += words[j],
        suffix = words[i+n]
        prefixes.setdefault(prefix, set()).add(suffix)

    return prefixes


def get_prefix(suffix, *args):
    '''Generates new prefix for Markov Analysis text generation. 

    suffix: string
    args: tuple of strings

    returns: tuple of strings
    '''
    return args[1:] + (suffix,)


def get_suffix(prefixes, prefix):
    '''Generates random suffix from prefixes.

    prefixes: mapping from prefix to suffixes
    prefix: tuple of strings

    returns: string
    '''
    return random.choice(list(prefixes[prefix]))


def print_next(prefixes, prefix):
    '''Generates next prefix and suffix pairing, printing the suffix.
    '''
    suffix = get_suffix(prefixes, prefix)
    prefix = get_prefix(suffix, *prefix)
    print(suffix, end=' ')
    return prefix


def print_next_recursive(prefixes, prefix, i):
    '''Recursive version of print_next. Hits max recursion depth if too long,
    so opted for print_next using for loop.

    i: int of times to run
    '''
    if i <= 0:
        return
    suffix = get_suffix(prefixes, prefix)
    prefix = get_prefix(suffix, *prefix)
    print(suffix, end=' ')
    print_next_recursive(prefixes, prefix, i-1)


def generate_markov(filename, prefix_length=2, words=100, punc=True, skiphead=True, lower=False):
    '''Runs text generation based on Markov analysis.

    text: str
    prefix_length: int
    words: int
    punc: bool. Set to False to remove punctuation from generated text
    skiphead: bool. Set to False if not gutenberg text
    '''
    word_list = get_words(filename, skiphead=skiphead,
                          allow_punc=punc, lower=lower)
    # Generate dictionary mapping prefixes to suffixes
    prefixes = perform_markov(word_list, prefix_length)

    # Choose first prefix to begin
    prefix = random.choice(list(prefixes))

    # Print first words
    for word in prefix:
        print(word, end=' ')

    # Recursive version for learning purposes. Hits max recursion depth
    # print_next_recursive(prefixes, prefix, words)

    # Generate and print words
    for i in range(words):
        prefix = print_next(prefixes, prefix)


def generate_mashup(*filenames, prefix_length=2, words=100):
    '''Runs text generation with two files.
    '''
    word_list = []
    for f in filenames:
        word_list += get_words(f, allow_punc=True, lower=False, numskip=True)

    prefixes = perform_markov(word_list, prefix_length)
    prefix = random.choice(list(prefixes))

    for word in prefix:
        print(word, end=' ')

    for i in range(words):
        prefix = print_next(prefixes, prefix)


def ex13_8():
    '''Run Markov analysis solution.
    '''
    print('Bee:')
    generate_markov('resources/bee.txt', words=10, skiphead=False)

    print('\n\nGrimm:')
    generate_markov('resources/grimm.txt', prefix_length=4)

    markov1 = "‘see, what a blockhead that brother of mine is! he will tear you in such and such dirty walking they could not, however, reach the castle lived an old mouse hole. ‘good night, my masters!’ said he, ‘but a white handkerchief out of yonder brook, for i wish for a moment; but the heat grew greater as soon as day dawned the two elder brothers would have slept soundly enough.’ when they took up a long while after, he went merrily home. the wedding feast was announced, the youth again said quite sadly: ‘if i had caught itself in the air!’"

    print('\n\nEmma, Beowulf and Frankenstein mashup:')
    filenames = ('resources/emma.txt', 'resources/beowulf.txt',
                 'resources/frankenstein.txt')
    generate_mashup(*filenames, prefix_length=2, words=500)


# 13.9. The “rank” of a word is its position in a list of words sorted by frequency:
# the most common word has rank 1, the second most common has rank 2, etc.
#
# Zipf’s law describes a relationship between the ranks and frequencies of words
# in natural languages (http://en.wikipedia.org/wiki/Zipf's_law). Specifically,
# it predicts that the frequency, f , of the word with rank r is:
#
#	f=cr^(−s)
#
# where s and c are parameters that depend on the language and the text.
# If you take the logarithm of both sides of this equation, you get:
#
#	log f = log c − s log r
#
# So if you plot log f versus log r, you should get a straight line with
# slope −s and intercept log c.
# 
# Write a program that reads a text from a file, counts word frequencies,
# and prints one line for each word, in descending order of frequency, with
# log f and log r. Use the graphing program of your choice to plot the results
# and check whether they form a straight line. Can you estimate the value of s?



# Run solutions
# ex13_1()
# ex13_2()
# ex13_3()
# ex13_4()
# ex13_5()
# ex13_6()
# ex13_7()
ex13_8()
