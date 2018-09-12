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

def open_file(filename):
    return open(filename, encoding='UTF-8').read()
    
s = open_file('12. Tuples/goldenbird.txt')

s = s[:400]

t = s.split()

for i in range(len(t)):
    t[i] = t[i].lower()
    for punctuation in string.punctuation:
        if punctuation in t[i]:
            t[i] = t[i].replace(punctuation, '')

print(t)