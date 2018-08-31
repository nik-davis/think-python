#                                                                      #
# --------------------Chapter 11: Dictionaries------------------------ #
#                                                                      #

# 11.1. Write a function that reads the words in words.txt and stores them
# as keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the dictionary.


import time


def in_bisect(word_list, word):
    '''Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string

    returns: True if the word is in the list; False otherwise
    '''
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word == word_list[i]:
        return True

    if word < word_list[i]:
        # Search first half
        return in_bisect(word_list[:i], word)
    else:
        # Search second half
        return in_bisect(word_list[i+1:], word)


def build_word_list():
    '''Builds word list from text file

    returns: list of strings
    '''
    fin = open('words.txt')
    word_list = []

    for line in fin:
        word = line.strip()
        word_list.append(word)

    return word_list


def build_word_dict():
    '''Read words in words.txt and store them as keys in a dictionary'''
    word_dict = dict()
    fin = open('words.txt')

    for line in fin:
        word = line.strip()
        word_dict[word] = 1

    return word_dict

def ex11_1():
    '''Compare search speeds in different storage types'''
    word_dict = build_word_dict()

    start_time = time.time()
    'zombies' in word_dict
    run_time = time.time() - start_time
    print(run_time)

    word_list = build_word_list()

    start_time = time.time()
    in_bisect(word_list, 'zombies')
    run_time = time.time() - start_time
    print(run_time)

    start_time = time.time()
    'zombies' in word_list
    run_time = time.time() - start_time
    print(run_time)


# 11.2. Read the documentation of the dictionary method setdefault and 
# use it to write a more concise version of invert_dict.
# setdefault(key[, default])
# If key is in the dictionary, return its value. If not, insert key with
# a value of default and return default. default defaults to None.


def histogram(s):
    '''Create histogram
    '''
    d = dict()
    for c in s:
        d[c] = d.get(c, 0)
        d[c] += 1
    return d


def invert_dict_orig(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
        # inverse[val] += [key]
    return inverse

hist = histogram('parrot')
print(hist)

print(invert_dict(hist))
print(invert_dict_orig(hist))


# ex11_1()