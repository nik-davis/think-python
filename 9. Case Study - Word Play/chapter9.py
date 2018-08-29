#                                                                     #
# ---------------------- Chapter 9 Exercises ------------------------ #
#                                                                     #

# 9.1. Write a program that reads words.txt and prints only the words 
# with more than 20 characters (not counting whitespace).

def ex9_1():
    fin = open('words.txt')
    output = ''

    for line in fin:
        word = line.strip()
        if len(word) > 20:
            output = output + word + ' '
    
    print('9.1. Words with more than 20 characters:', output)

# 9.2. Write a function called has_no_e that returns True if the given 
# word doesn’t have the letter “e” in it. Modify your program from the 
# previous section to print only the words that have no “e” and compute 
# the percentage of the words in the list that have no “e”. 

def has_no_e(word):
    if 'e' not in word:  # alt: for letter in word, if letter == 'e'
        return True
    return False

def ex9_2():
    fin = open('words.txt')
    count = 0
    total = 0

    for line in fin:
        word = line.strip()
        if has_no_e(word):
            # print(word)
            count += 1
        total += 1
    percent = round(count * 100 / total, 2)
    print('9.2.', percent, "% of the words contain e. That's", count, 'words!')

# 9.3. Write a function named avoids that takes a word and a string of 
# forbidden letters, and that returns True if the word doesn’t use any 
# of the forbidden letters. 
# 
# Modify your program to prompt the user to enter a string of forbidden 
# letters and then print the number of words that don’t contain any of 
# them. Can you find a combination of 5 forbidden letters that excludes 
# the smallest number of words?

def avoids(word, forbidden):
    for f in forbidden:      # alt: for l in word, if l in forbidden
        if f in word:
            return False
    return True


def ex9_3():
    maxsofar = 0
    while True:
        forbidden = input('9.3. Enter string of forbidden letters (type "safeword" to stop): ')
        if forbidden == 'safeword':
            break

        count = 0
        fin = open('words.txt')

        for line in fin:
            word = line.strip()
            
            if avoids(word, forbidden):
                count += 1

        if count > maxsofar:
            maxsofar = count
        print('  Count:', count, '\n  Max so far:', maxsofar)
    
# 9.4. Write a function named uses_only that takes a word and a string 
# of letters, and that returns True if the word contains only letters in
# the list. Can you make a sentence using only the letters acefhlo?

def uses_only(word, letters):
    for w in word:
        if w not in letters:
            return False
    return True

def ex9_4():
    fin = open('words.txt')

    word_list = []

    for line in fin:
        word = line.strip()
        if uses_only(word, 'acefhlo'):
            word_list.append(word)

    if input('9.4. Print acefhlo words list? (y/n): ') == 'y':
        print(word_list)

# 9.5. Write a function named uses_all that takes a word and a string of
# required letters, and that returns True if the word uses all the requ-
# ired letters at least once. How many words are there that use all the
# vowels aeiou? How about aeiouy? 

def uses_all(word, letters):
    for l in letters:
        if l not in word:
            return False
    return True             # alt: return uses_only(letters, word)

def ex9_5():
    fin = open('words.txt')

    count = 0
    letters = 'aeiuoy'
    words_list = []

    for line in fin:
        word = line.strip()
        if uses_all(word, letters):
            count += 1
            words_list.append(word)
    
    print('9.5.', count, 'words use all letters', letters, end='. ')
    if input('Show words? (y/n): ') == 'y':
        print(words_list)
    
# 9.6. Write a function called is_abecedarian that returns True if the 
# letters in a word appear in alphabetical order (double letters are ok).
# How many abecedarian words are there?

def is_abecedarian(word):
    word = word.lower()
    previous_w = 'a' # = word[0]

    for w in word:
        if w < previous_w:
            return False
        previous_w = w

    return True

def ex9_6():
    fin = open('words.txt')
    count = 0
    word_list = []

    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            word_list.append(word)
            count += 1

    print('9.6.', count, 'words are abecedarian.', end=' ')
    if input('Show words? (y/n): ') == 'y':
        print(word_list)

# 9.7. Give me a word with three consecutive double letters. I’ll give 
# you a couple of words that almost qualify, but don’t. For example, the 
# word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ 
# that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-ip-p-i. If you could 
# take out those i’s it would work. But there is a word that has three 
# consecutive pairs of letters and to the best of my knowledge this may 
# be the only word. Of course there are probably 500 more but I can only 
# think of one. What is the word?

def three_in_row(word):
    i = 0

    while i < len(word) - 5:
        if word[i] == word[i+1]:
            if word[i+2] == word[i+3]:
                if word[i+4] == word[i+5]:
                    return True            
        i += 1

    return False

def is_triple_double(word):
    """Solution given: Tests if a word contains three consecutive double letters.
    
    word: string

    returns: bool
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False

def ex9_7():
    fin = open('words.txt')

    for line in fin:
        word = line.strip()
        if three_in_row(word):
            print(word)
    

# 9.8. “I was driving on the highway the other day and I happened to 
# notice my odometer. Like most odometers, it shows six digits, in whole
# miles only. So, if my car had 300,000 miles, for example, I’d see 3-0-0-0-0-0.
#
# “Now, what I saw that day was very interesting. I noticed that the last 
# 4 digits were palindromic; that is, they read the same forward as backward. 
# For example, 5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5. 
# 
# “One mile later, the last 5 numbers were palindromic. For example, it 
# could have read 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 
# numbers were palindromic. And you ready for this? One mile later, all 6 were palindromic! 
# 
# “The question is, what was on the odometer when I first looked?” 
#
# Write a Python program that tests all the six-digit numbers and prints 
# any numbers that satisfy these requirements

def has_palindrome():
    return False

def check(i):
    return False

def check_all():
    return False

def is_palindromic(string):
    i = 0
    j = len(string) - 1

    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True

def ex9_8():
    for i in range(100000, 999996):
        if is_palindromic(str(i)[2:]):
            if is_palindromic(str(i+1)[1:]):
                if is_palindromic(str(i+2)[1:5]):
                    if is_palindromic(str(i+3)):
                        print(i)

# 9.9. “Recently I had a visit with my mom and we realized that the two 
# digits that make up my age when reversed resulted in her age. For example, 
# if she’s 73, I’m 37. We wondered how often this has happened over the 
# years but we got sidetracked with other topics and we never came up with an answer.
#	
# “When I got home I figured out that the digits of our ages have been 
# reversible six times so far. I also figured out that if we’re lucky it 
# would happen again in a few years, and if we’re really lucky it would 
# happen one more time after that. In other words, it would have happened 
# 8 times over all. So the question is, how old am I now?”
#
# Write a Python program that searches for solutions to this Puzzler. 
# Hint: you might find the string method zfill useful.

def reverse_check(age1, age2):
    if age1 == age2[1]+age2[0]:
        return True
    return False

def check_one_age_gap(age1, age2):
    count = 0

    while age2 < 100:
        age1_str = str(age1).zfill(2)
        age2_str = str(age2).zfill(2)
        if reverse_check(age1_str, age2_str):
            count  += 1
        
        age1 += 1
        age2 += 1
    
    return count

def check_all_gaps(num_reversals):
    age1 = 0
    age2 = 16
    while age2 < 100:
        reversals = check_one_age_gap(age1, age2)
        if reversals == num_reversals:
            output = age2

        age2 += 1
    return output

def ex9_9():
    age1 = 0
    age2 = check_all_gaps(8)
    age_gap = age2
    count = 0

    while age2 < 100:
        age1_str = str(age1).zfill(2)
        age2_str = str(age2).zfill(2)
        if reverse_check(age1_str, age2_str):
            count  += 1
        if count == 6:
            age1_lower = age1
        if count == 7:
            age1_upper = age1
        age1 += 1
        age2 += 1

    print('Child is between', age1_lower, 'and', age1_upper, 'years old.')
    print('Mother is', age_gap, 'years older.')


ex9_1()
ex9_2()
ex9_3()
ex9_4()
ex9_5()
ex9_6()
ex9_7()
ex9_8()
ex9_9()


# TODO: Modify ex7-ex9 for better output
# TODO: Modify ex7 and ex8 for better encapsulation
# TODO: Modify ex9 to check for two possibilities in a year
