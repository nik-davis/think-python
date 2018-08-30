#                                                                      #
# -----------------------Chapter 10: Lists---------------------------- #
#                                                                      #

# 10.1. Write a function called nested_sum that takes a list of lists of
# integers and adds up the elements from all of the nested lists. For example:
#   >>> t = [[1, 2], [3], [4, 5, 6]]
#   >>> nested_sum(t)
#   21


def my_sum(t):
    '''Returns the sum of items in a list

    t: List

    returns: List
    '''
    total = 0
    for s in t:
        total += s
    return total


def nested_sum(t):
    '''Calculates, prints and returns the sum of all elements within a
    nested list

    t: List

    returns: List
    '''
    total = 0
    for s in t:
        total += my_sum(s)
    print(total)
    return total


def ex10_1():
    t = [[1, 2], [3], [4, 5, 6]]
    nested_sum(t)

# 10.2 Write a function called cumsum that takes a list of numbers and
# returns the cumulative sum; that is, a new list where the ith element
# is the sum of the first i + 1 elements from the original list. For example:
#   >>> t = [1, 2, 3]
#   >>> cumsum(t)
#   [1, 3, 6]


def cumsum(t):
    '''Returns cumulative sum of a list of numbers

    t: List

    returns: List
    '''
    s = []

    for i in range(len(t)):
        if i == 0:
            s.append(t[i])
        else:
            s.append(s[i-1]+t[i])

    return s


def ex10_2():
    print(cumsum([1, 2, 3]))

# 10.3. Write a function called middle that takes a list and returns a
# new list that contains all but the first and last elements. For example:
#   >>> t = [1, 2, 3, 4]
#   >>> middle(t)
#   [2, 3]


def middle(t):
    '''Takes a list and returns a new list containing all but the first
    and last elements

    t: List

    returns: List
    '''
    s = t[1:len(t)-1]
    return s


def ex10_3():
    t = [1, 2, 3, 4]
    middle_t = middle(t)
    print('t:', t, 'middle(t):', middle_t)

# 10.4. Write a function called chop that takes a list, modifies it by
# removing the first and last elements, and returns None. For example:
#   >>> t = [1, 2, 3, 4]
#   >>> chop(t)
#   >>> t
#   [2, 3]


def chop(t):
    '''Takes a list and removes the first and last elements of that list

    t: List

    returns: None
    '''
    if len(t) > 1:
        t.pop(0)    # del t[0]
        t.pop()     # del t[len(t)-1]


def ex10_4():
    t = [1, 2, 3, 4]
    chop_t = chop(t)
    print('t:', t, '\tchop(t):', chop_t)

# 10.5.  Write a function called is_sorted that takes a list as a parameter
# and returns True if the list is sorted in ascending order and False otherwise.
#   >>> is_sorted([1, 2, 2])
#	True
#	>>> is_sorted(['b', 'a'])
#   False


def is_sorted(t):
    '''Returns True if a list is sorted in ascending order, and False otherwise

    t: list

    returns: Bool
    '''

    for i in range(len(t)-1):
        if t[i] > t[i+1]:
            return False
    return True


def ex10_5():
    a = [1, 2, 2]
    b = ['b', 'a']
    print('a:', a, ' is sorted?', is_sorted(a))
    print('b:', b, 'is sorted?', is_sorted(b))

# 10.6. Two words are anagrams if you can rearrange the letters from one
# to spell the other. Write a function called is_anagram that takes two
# strings and returns True if they are anagrams.


def is_anagram(word1, word2):
    '''Takes two strings and returns True if they are anagrams, False otherwise

    word1, word2: String

    returns: Bool
    '''

    if sorted(word1.replace(' ', '')) == sorted(word2.replace(' ', '')):
        return True
    return False


def scan_words():
    '''Scan words in words.txt and print out anagrams. Takes a very long time
    '''

    fin = open('10. Lists\words.txt')
    word_list = []
    for line in fin:
        word = line.strip()
        word_list.append(word)

    for word1 in word_list:
        for word2 in word_list:
            if word1 == word2:
                pass
            elif is_anagram(word1, word2):
                print(word1, word2)


def ex10_6():
    print('10.6. Anagram tests:')
    print('  abc & cba:', is_anagram('abc', 'cba'))
    print('  abc & ccc:', is_anagram('abc', 'ccc'))
    print('  aabc & abbc:', is_anagram('aabc', 'abbc'))
    if input('Scan words list (y/n)?: ') == 'y':
        scan_words()

# 10.7. Write a function called has_duplicates that takes a list and
# returns True if there is any element that appears more than once.
# It should not modify the original list.


def has_duplicates(t):
    '''Returns True if any element in a list appears more than once, False otherwise

    t: list

    returns: Bool
    '''

    for word1 in t:
        count = 0
        for word2 in t:
            if word1 == word2:
                count += 1
        if count > 1:
            return True
    return False


def ex10_7():
    print('10.7. Duplicates Test:')
    word_list = 'cat dog bear snake cow'.split()
    print(' ', word_list, has_duplicates(word_list))
    word_list = 'cat dog bear snake dog'.split()
    print(' ', word_list, has_duplicates(word_list))

# 10.8. If there are 23 students in your class, what are the chances that
# two of you have the same birthday? You can estimate this probability
# by generating random samples of 23 birthdays and checking for matches.
# Hint: you can generate random birthdays with the randint function in the random module.


from random import randint


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


def rand_birthdays(n):
    '''Generates a list of random integers from 1 to 366, of length n

    n : int

    returns: list of int
    '''

    birthdays = []

    for b in range(n):
        birthdays.append(randint(1, 366))

    return birthdays


def count_matches(num_iter=1000, num_people=23):
    '''Generates a sample of birthdays and counts duplicates

    num_iter: how many iterations to run
    num_people: how many people in each sample

    returns: int
    '''

    count = 0
    total = 0

    for i in range(num_iter):
        birthdays = rand_birthdays(num_people)

        if has_duplicates(birthdays):
            count += 1

        total += 1

    matches = round(count * 100 / total, 1)

    return matches


def ex10_8():
    '''Runs birthday simulation and prints results'''

    print('10.8. Testing Birthday Paradox:')
    num_tests = 10  # int(input(' Run how many tests (~10)?: '))
    num_iter = 1000  # int(input(' How many iterations per test (~1000)?: '))
    num_people = 23  # int(input(' And how many people to simulate (~23)?: '))

    average_total = 0

    for t in range(num_tests):
        matches = count_matches(num_iter, num_people)

        average_total += matches

        output = '  Test {0}: Probability after {1} iterations is {2}%'.format(
            str(t+1).zfill(2), num_iter, matches)
        print(output)

    average = round(average_total / num_tests, 1)
    print(' Average probability after {0} tests is {1}%'.format(
        num_tests, average))



# Run solutions
# ex10_1()
# ex10_2()
# ex10_3()
# ex10_4()
# ex10_5()
# ex10_6()
# ex10_7()
ex10_8()
