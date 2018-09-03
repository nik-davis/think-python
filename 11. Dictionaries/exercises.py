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
    '''Inverts a dictionary, returning a map from val to a list of keys.

    If the mapping key->val appears in d, then in the new dictionary
    val maps to a list that includes key.

    d: dict
    
    Returns: dict
    '''
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
        # d.setdefault(val, []) == d['val']
    return inverse


def get_example():
    '''Frequently you will see code create a variable, assign a default 
    value to the variable, and then check a dict for a certain key. 
    If the key exists, then the value of the key is copied into the value 
    for the variable. 
    
    While there is nothing wrong this, it is more concise to use the 
    built-in method dict.get(key[, default]) from the Python Standard 
    Library. If the key exists in the dict, then the value for that key 
    is returned. If it does not exist, then the default value 
    specified as the second argument to get() is returned
    
    dict.get(key[, default])
    '''
    dictionary = {'message': 'hello world'}

    # Verbose and inefficient method
    #  The code below initializes a variable called data to an empty string. 
    #  Then it checks if a certain key called message exists in a dict 
    #  called dictionary. If the key exists, then the value of that key is 
    #  copied into the data variable.
    data = ''

    if 'message' in dictionary:
        data = dictionary['message']
    
    # Using get
    #  When get() is called, Python checks if the specified key exists in 
    #  the dict. If it does, then get() returns the value of that key. 
    #  If the key does not exist, then get() returns the value specified 
    #  in the second argument to get().
    data = dictionary.get('message', '')

    print(data)


def setdefault_example():
    '''When initializing a dictionary, it is common to see a code check 
    for the existence of a key and then create the key if it does not exist. 
    Although there is nothing wrong with this, the exact same idea can be 
    accomplished more concisely by using the built-in dictionary method setdefault().
    
    dict.setdefault(key[, default])
    '''
    dictionary = {}

    # Verbose and inefficient method:
    #  The code below checks if a key named list exists in a dictionary 
    #  called dictionary. If it does not exist, then the code creates the
    #  key and then sets its value to an empty list. The code then proceeds
    #  to append a value to the list
    if "list" not in dictionary:
        dictionary["list"] = []

    dictionary["list"].append("list_item")

    dictionary = {}

    # Using setdefault:
    #  The modified code below uses setdefault() to initialize the dictionary.
    #  When setdefault() is called, it will check if the key already exists.
    #  If it does exist, then setdefault() does nothing. If the key does not
    #  exist, then setdefault() creates it and sets it to the value specified
    #  in the second argument.
    dictionary.setdefault("list", []).append("list_item")

    print(dictionary)


def ex11_2():
    d = dict(a=1, b=2, c=3, z=1)
    print('d:', d)
    inverse = invert_dict(d)
    print('inverse:', inverse)
    for val in inverse:
        keys = inverse[val]
        print(val, keys)

    hist = histogram('parrot')
    print(hist)

    print(invert_dict(hist))
    print(invert_dict_orig(hist))

    get_example()
    setdefault_example()


# 11.3. Memoize the Ackermann function from Exercise 6.2 and see if memoization
# makes it possible to evaluate the function with bigger arguments. Hint: no. 


known = {}

def ack(m, n):
    '''Compute Ackermann function A(m, n)
    
    n, m: non-negative int
    '''
    key = str(m) + '-' + str(n)
    if key in known:
        return known[key]

    if m == 0:
        result = n + 1
    elif m > 0 and n == 0:
        result = ack(m-1, 1)
    elif m > 0 and n > 0:
        result =  ack(m-1, ack(m, n-1))
    
    known[key] = result
    return result


cache = {}

def ackermann_solution(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)

    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]


def ex11_3():
    print('ack(3,4) = 125: ', ack(3, 4))
    print(ack(0,1))
    print(ack(1,0))
    print(ack(0,0))
    print(known)


# 10.4. Use a dictionary to write a faster, simpler version of has_duplicates.


def has_duplicates(t):
    '''Returns True if any element appears more than once in a sequence.
    (Only iterates through one loop so should be faster, but has to run sort)

    t: list

    returns: bool
    '''
    # make a copy of t to avoid modifying the parameter
    s = t[:]
    s.sort()

    # check for adjacent elements that are equal
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def has_duplicates(t):
    '''Returns true if any element appears more than once

    t: list
    '''
    d = {}
    for item in t:
        if item in d:
            return True
        d[item] = 1
    return False
    

def has_duplicates_solution(t):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.

    t: sequence
    """
    return len(set(t)) < len(t)


def ex10_4():
    t = [1, 2, 3]
    print(has_duplicates(t))
    t.append(3)
    print(has_duplicates(t))

    t = [1, 2, 3]
    print(has_duplicates_solution(t))
    t.append(3)
    print(has_duplicates_solution(t))


# 11.5. Two words are “rotate pairs” if you can rotate one of them and get 
# the other. Write a program that reads a wordlist and finds all the rotate pairs.


def rotate_letter(letter, n):
    '''Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    '''
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
    '''Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    '''
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


def rotate_pairs(word_dict):
    '''Saves all rotate pairs to a dictionary
    
    word_dict: dictionary with words as keys
    
    Returns: dict
    '''
    rotate_dict = {}
    for word in word_dict:
        for i in range(1, 14):
            rotated_word = rotate_word(word, i)
            if rotated_word in word_dict:
                rotate_dict.setdefault(word, []).append(rotated_word)
                rotate_dict[word].append(i)

    return rotate_dict


def ex11_5():
    '''Find all rotate pairs in word_dict, save them to a dict and print'''
    word_dict = build_word_dict()
    # word_dict = {'zips': None, 'lube': None}
    
    rotate_dict = rotate_pairs(word_dict)
    
    print(rotate_dict)


# 11.6. But there is, however, at least one word that Dan and we know of, 
# which will yield two homophones if you remove either of the first two 
# letters to make two, new four-letter words. The question is, what’s the word?
# Write a program that lists all the words that solve the Puzzler.


from pronounce import read_dictionary


def ex11_6():
    '''Uses a lot of if statements to check for solutions to homophone puzzle
    '''
    phonetic_d = read_dictionary('c06d.txt')
    word_dict = build_word_dict()
    word_list = ['wrack']
    for word in word_dict:
        word1 = word[1:]
        word2 = word[0] + word[2:]
        if word1 in word_dict and word2 in word_dict:
            if word in phonetic_d and word1 in phonetic_d and word2 in phonetic_d:
                if phonetic_d[word] == phonetic_d[word1] == phonetic_d[word2]:
                    print(word, word1, word2)


# ex11_1()
# ex11_2()
# ex11_3()
# ex10_4()
# ex11_5()
ex11_6()