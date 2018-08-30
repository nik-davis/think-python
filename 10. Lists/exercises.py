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

    fin = open('10. Lists/words.txt')
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


# 10.9. Write a function that reads the file words.txt and builds a list
# with one element per word. Write two versions of this function, one
# using the append method and the other using the idiom t = t + [x].
# Which one takes longer to run? Why?


import time


def build_list_a():
    '''Reads lines from a file and builds a list, using append'''
    fin = open('10. Lists/words.txt')

    t = []

    for line in fin:
        word = line.strip()
        t.append(word)

    return t


def build_list_b():
    '''Reads lines from a file and builds a list, using + '''
    fin = open('10. Lists/words.txt')

    t = []

    for line in fin:
        word = line.strip()
        t = t + [word]

    return t


def ex10_9():
    print('10.9. Testing list building:')

    print(' Append:')
    start_time = time.time()
    a = build_list_a()
    elapsed_time = round(time.time() - start_time, 2)

    print('  Length:', len(a))
    print('  First ten elements:', a[:10])
    print('  Time taken:', elapsed_time, 'seconds.')

    print(' Using +:')
    start_time = time.time()
    b = build_list_b()
    elapsed_time = round(time.time() - start_time, 2)

    print('  Length:', len(b))
    print('  First ten elements:', b[:10])
    print('  Time taken:', elapsed_time, 'seconds.')


# 10.10. Write a function called in_bisect that takes a sorted list and a
# target value and returns True if the word is in the list and False if it’s not.


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


def in_bisect_alt(word_list, word):
    '''From solution: Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    '''
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


def ex10_10():
    t = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    word = '2'

    s = t[:]
    s.sort()

    print(in_bisect(t, word))


# 10.11. Two words are a “reverse pair” if each is the reverse of the other.
# Write a program that finds all the reverse pairs in the word list.


def build_word_list():
    '''Builds word list from text file

    returns: list of strings
    '''
    fin = open('10. Lists/words.txt')
    word_list = []

    for line in fin:
        word = line.strip()
        word_list.append(word)

    return word_list


def is_reverse_pair(word1, word2):
    '''First attempt at verifying reverse pairs. Too slow.'''
    return word1 == word2[::-1]

def find_pairs():
    '''Populate pair list with all reverse-word pairs
    
    returns: list of strings
    '''
    pair_list = []

    # Slow, obsolete:
    # for word1 in word_list:
    #     for word2 in word_list:
    #         if word1 != word2:
    #             if is_reverse_pair(word1, word2):
    #                 print(word1, word2)
    #                 pair_list.append(word1)

    for word1 in word_list:
        if in_bisect(word_list, word1[::-1]) and word1 != word1[::-1]:
            if word1 not in pair_list:
                pair_list.append(word1)
            if word1[::-1] not in pair_list:
                pair_list.append(word1[::-1])
    return pair_list

def ex10_11():
    '''pair_list given as search takes a while, run find_pairs() instead for new search'''
    word_list = build_word_list()
    # find_pairs()
    pair_list = ['abut', 'tuba', 'ad', 'da', 'ados', 'soda', 'agar', 'raga', 'agas', 'saga', 'agenes', 'senega', 'ah', 'ha', 'aider', 'redia', 'airts', 'stria', 'ajar', 'raja', 'alif', 'fila', 'am', 'ma', 'amen', 'nema', 'amis', 'sima', 'an', 'na', 'anger', 'regna', 'animal', 'lamina', 'animes', 'semina', 'anon', 'nona', 'ante', 'etna', 'are', 'era', 'ares', 'sera', 'aril', 'lira', 'arris', 'sirra', 'arum', 'mura', 'at', 'ta', 'ate', 'eta', 'ates', 'seta', 'auks', 'skua', 'avid', 'diva', 'avo', 'ova', 'ay', 'ya', 'bad', 'dab', 'bag', 'gab', 'bal', 'lab', 'bals', 'slab', 'ban', 'nab', 'bard', 'drab', 'bas', 'sab', 'bat', 'tab', 'bats', 'stab', 'bed', 'deb', 'ben', 'neb', 'bid', 'dib', 'big', 'gib', 'bin', 'nib', 'bins', 'snib', 'bird', 'drib', 'bis', 'sib', 'bog', 'gob', 'bos', 'sob', 'bots', 'stob', 'bows', 'swob', 'brad', 'darb', 'brag', 'garb', 'bud', 'dub', 'bun', 'nub', 'buns', 'snub', 'bur', 'rub', 'burd', 'drub', 'burg', 'grub', 'bus', 'sub', 'but', 'tub', 'buts', 'stub', 'cam', 'mac', 'cap', 'pac', 'cares', 'serac', 'cod', 'doc', 'cram', 'marc', 'cud', 'duc', 'dag', 'gad', 'dah', 'had', 'dahs', 'shad', 'dam', 'mad', 'dap', 'pad', 'dart', 'trad', 'daw', 'wad', 'debut', 'tubed', 'decal', 'laced', 'dedal', 'laded', 'deem', 'meed', 'deep', 'peed', 'deeps', 'speed', 'deer', 'reed', 'dees', 'seed', 'defer', 'refed', 'degami', 'imaged', 'deifier', 'reified', 'deil', 'lied', 'deke', 'eked', 'del', 'led', 'delf', 'fled', 'deliver', 'reviled', 'dels', 'sled', 'demit', 'timed', 'denier', 'reined', 'denies', 'seined', 'denim', 'mined', 'dens', 'sned', 'depot', 'toped', 'depots', 'stoped', 'derat', 'tared', 'derats', 'stared', 'dessert', 'tressed', 'desserts', 'stressed', 'devas', 'saved', 'devil', 'lived', 'dew', 'wed', 'dewans', 'snawed', 'dexes', 'sexed', 'dial', 'laid', 'dialer', 'relaid', 'diaper', 'repaid', 'dig', 'gid', 'dim', 'mid', 'dinar', 'ranid', 'diols', 'sloid', 'dirts', 'strid', 'do', 'od', 'dog', 'god', 'dom', 'mod', 'don', 'nod', 'doom', 'mood', 'door', 'rood', 'dor', 'rod', 'dormin', 'nimrod', 'dorp', 'prod', 'dos', 'sod', 'dot', 'tod', 'drail', 'liard', 'draw', 'ward', 'drawer', 'reward', 'draws', 'sward', 'dray', 'yard', 'dual', 'laud', 'ducs', 'scud', 'duel', 'leud', 'duo', 'oud', 'dup', 'pud', 'dups', 'spud', 'eat', 'tae', 'edile', 'elide', 'edit', 'tide', 'eel', 'lee', 'eh', 'he', 'elides', 'sedile', 'em', 'me', 'emes', 'seme', 'emir', 'rime', 'emit', 'time', 'emits', 'stime', 'enol', 'lone', 'er', 're', 'ergo', 'ogre', 'eros', 'sore', 'ervil', 'livre', 'etas', 'sate', 'even', 'neve', 'evil', 'live', 'eviler', 'relive', 'fer', 'ref', 'fires', 'serif', 'flog', 'golf', 'flow', 'wolf', 'fool', 'loof', 'gal', 'lag', 'gals', 'slag', 'gam', 'mag', 'gan', 'nag', 'gar', 'rag', 'gas', 'sag', 'gat', 'tag', 'gats', 'stag', 'gel', 'leg', 'gelder', 'redleg', 'get', 'teg', 'gip', 'pig', 'girt', 'trig', 'gnar', 'rang', 'gnat', 'tang', 'gnats', 'stang', 'gnaws', 'swang', 'gnus', 'sung', 'got', 'tog', 'gul', 'lug', 'gulp', 'plug', 'guls', 'slug', 'gum', 'mug', 'gums', 'smug', 'guns', 'snug', 'gut', 'tug', 'habus', 'subah', 'hahs', 'shah', 'hales', 'selah', 'hap',
                 'pah', 'hay', 'yah', 'hey', 'yeh', 'ho', 'oh', 'hoop', 'pooh', 'hop', 'poh', 'is', 'si', 'it', 'ti', 'jar', 'raj', 'kay', 'yak', 'keel', 'leek', 'keels', 'sleek', 'keep', 'peek', 'keets', 'steek', 'kips', 'spik', 'knaps', 'spank', 'knar', 'rank', 'knits', 'stink', 'lager', 'regal', 'lair', 'rial', 'lap', 'pal', 'lares', 'seral', 'larum', 'mural', 'las', 'sal', 'leer', 'reel', 'lees', 'seel', 'leets', 'steel', 'leper', 'repel', 'lever', 'revel', 'levins', 'snivel', 'liar', 'rail', 'lin', 'nil', 'lion', 'noil', 'lit', 'til', 'lobo', 'obol', 'loom', 'mool', 'loons', 'snool', 'loop', 'pool', 'loops', 'spool', 'loot', 'tool', 'looter', 'retool', 'loots', 'stool', 'lop', 'pol', 'lotos', 'sotol', 'macs', 'scam', 'maes', 'seam', 'map', 'pam', 'mar', 'ram', 'marcs', 'scram', 'mart', 'tram', 'mat', 'tam', 'maws', 'swam', 'may', 'yam', 'meet', 'teem', 'meter', 'retem', 'mho', 'ohm', 'mils', 'slim', 'mir', 'rim', 'mis', 'sim', 'mon', 'nom', 'moor', 'room', 'moot', 'toom', 'mot', 'tom', 'mures', 'serum', 'mus', 'sum', 'muts', 'stum', 'namer', 'reman', 'nap', 'pan', 'naps', 'span', 'neep', 'peen', 'net', 'ten', 'neves', 'seven', 'new', 'wen', 'nip', 'pin', 'nips', 'spin', 'nit', 'tin', 'no', 'on', 'nolos', 'solon', 'nos', 'son', 'not', 'ton', 'notes', 'seton', 'now', 'won', 'nu', 'un', 'nus', 'sun', 'nut', 'tun', 'nuts', 'stun', 'oat', 'tao', 'oohs', 'shoo', 'oot', 'too', 'os', 'so', 'ow', 'wo', 'pacer', 'recap', 'pals', 'slap', 'pans', 'snap', 'par', 'rap', 'part', 'trap', 'parts', 'strap', 'pas', 'sap', 'pat', 'tap', 'paw', 'wap', 'paws', 'swap', 'pay', 'yap', 'peels', 'sleep', 'pees', 'seep', 'per', 'rep', 'pets', 'step', 'pins', 'snip', 'pis', 'sip', 'pit', 'tip', 'pols', 'slop', 'pools', 'sloop', 'poons', 'snoop', 'port', 'trop', 'ports', 'strop', 'pot', 'top', 'pots', 'stop', 'pow', 'wop', 'pows', 'swop', 'prat', 'tarp', 'pupils', 'slipup', 'puris', 'sirup', 'pus', 'sup', 'put', 'tup', 'raps', 'spar', 'rat', 'tar', 'rats', 'star', 'raw', 'war', 'ray', 'yar', 'rebus', 'suber', 'rebut', 'tuber', 'recaps', 'spacer', 'redes', 'seder', 'redips', 'spider', 'redraw', 'warder', 'redrawer', 'rewarder', 'rees', 'seer', 'reflet', 'telfer', 'reflow', 'wolfer', 'reknit', 'tinker', 'reknits', 'stinker', 'relit', 'tiler', 'remeet', 'teemer', 'remit', 'timer', 'rennet', 'tenner', 'repins', 'sniper', 'res', 'ser', 'rot', 'tor', 'sallets', 'stellas', 'saps', 'spas', 'sat', 'tas', 'saw', 'was', 'scares', 'seracs', 'secret', 'terces', 'seeks', 'skees', 'selahs', 'shales', 'sirs', 'sris', 'sit', 'tis', 'six', 'xis', 'skeets', 'steeks', 'skips', 'spiks', 'sleeps', 'speels', 'sleets', 'steels', 'slit', 'tils', 'sloops', 'spools', 'smart', 'trams', 'smuts', 'stums', 'snaps', 'spans', 'snaw', 'wans', 'snaws', 'swans', 'snips', 'spins', 'snit', 'tins', 'snoops', 'spoons', 'snoot', 'toons', 'snot', 'tons', 'snow', 'wons', 'sow', 'wos', 'spat', 'taps', 'spay', 'yaps', 'spirt', 'trips', 'spirts', 'strips', 'spit', 'tips', 'sports', 'strops', 'spot', 'tops', 'spots', 'stops', 'sprat', 'tarps', 'sprits', 'stirps', 'staw', 'wats', 'stew', 'wets', 'stow', 'wots', 'stows', 'swots', 'straw', 'warts', 'strow', 'worts', 'struts', 'sturts', 'swat', 'taws', 'sway', 'yaws', 'swot', 'tows', 'tav', 'vat', 'taw', 'wat', 'tew', 'wet', 'tort', 'trot', 'tow', 'wot', 'trow', 'wort', 'way', 'yaw']
    
    if input('10.11. Display pairs list (y/n)?: ') == 'y':
        i = 0
        while i < len(pair_list) - 1:
            print(pair_list[i], pair_list[i+1])
            i += 2


# 10.12. Two words “interlock” if taking alternating letters from each forms 
# a new word. For example, “shoe” and “cold” interlock to form “schooled”.
#
#   1. Write a program that finds all pairs of words that interlock. 
#   Hint: don’t enumerate all pairs! 
#
#   2. Can you find any words that are three-way interlocked; that is, 
#   every third letter forms a word, starting from the first, second or third?






# Run solutions
# ex10_1()
# ex10_2()
# ex10_3()
# ex10_4()
# ex10_5()
# ex10_6()
# ex10_7()
# ex10_8()
# ex10_9()
# ex10_10()
# ex10_11()
