# -------------------------------------------------------------------- #
# ------------------------- Chapter 14. Files ------------------------ #
# -------------------------------------------------------------------- #

# 14.1. Write a function called sed that takes as arguments a pattern 
# string, a replacement string, and two filenames; it should read the 
# first file and write the contents into the second file (creating it 
# if necessary). If the pattern string appears anywhere in the file, it 
# should be replaced with the replacement string.
# 
# If an error occurs while opening, reading, writing or closing files, 
# your program should catch the exception, print an error message, and exit.


def sed(pattern, repl, source, output):
    '''Reads a source file a writes to output file. Replaces any existences of
    pattern with repl.

    pattern: string
    repl: string
    source: string filename
    output: string filename
    '''
    try:
        fin = open(source, 'r')
        fout = open(output, 'w')

        for line in fin:
            line = line.replace(pattern, repl)
            fout.write(line)

        fin.close()
        fout.close()
    except:
        print('An error occurred, but this program is too rudimentary to tell you what happened.')
        print('Have a nice day.')
        exit()


def ex14_1():
    pattern = 'monkey'
    repl = 'donkey'
    source = '14. Files/file.txt'
    output = source + '.replaced'

    print('Running sed...')
    sed(pattern, repl, source, output)
    print('...sed complete! No errors.')

    print('Running sed...')
    sed(pattern, repl, '14. Files/badfile.txt', output)
    print('...sed complete! No errors.')


# Exercise 14.2. If you download my solution to Exercise 12.2 from
# http://thinkpython2.com/code/anagram_sets.py, you’ll see that it 
# creates a dictionary that maps from a sorted string of letters to the 
# list of words that can be spelled with those letters. For example, 
# 'opst' maps to the list ['opts', 'post', 'pots', 'spot', 'stop', 'tops'].
#
# Write a module that imports anagram_sets and provides two new functions:
# store_anagrams should store the anagram dictionary in a “shelf”; 
# read_anagrams should look up a word and return a list of its anagrams.
#	Solution: http://thinkpython2.com/code/anagram_db.py.

import shelve

from anagram_sets import all_anagrams, signature


def store_anagrams(filename, anagram_map):
    '''Stores anagrams from a dictionary in a shelf.

    filename: string file name of shelf
    anagram_map: dictionary mapping strings to list of anagrams
    '''
    with shelve.open(filename, 'c') as db:
        for word, word_list in anagram_map.items():
            db[word] = word_list


def read_anagrams(word, db):
    '''Looks up word in shelf and returns list of its anagrams

    filename: string file name of shelf
    word: string to look up
    '''
    with shelve.open(db) as db:
        sig = signature(word)
        try:
            return db[sig]
        except:
            return []


def ex14_2():
    command='make_db'

    if command == 'make_db':
        # anagram_map = all_anagrams('resources/words.txt')
        anagram_map = dict()
        anagram_map['opst'] = ['opts', 'post', 'pots', 'spot', 'stop', 'tops']
        store_anagrams('14. Files/anagrams.db', anagram_map)

    print(read_anagrams('pots', '14. Files/anagrams.db'))


# Exercise 14.3. In a large collection of MP3 files, there may be more 
# than one copy of the same song, stored in different directories or with 
# different file names. The goal of this exercise is to search for duplicates.
#
#  1. Write a program that searches a directory and all of its subdirectories, 
#  recursively, and returns a list of complete paths for all files with a 
#  given suffix (like .mp3). Hint: os.path provides several useful functions 
#  for manipulating file and path names. 
#	
#  2. To recognize duplicates, you can use md5sum to compute a “checksum” 
#  for each files. If two files have the same checksum, they probably have 
#  the same contents.
#	
#  3. To double-check, you can use the Unix command diff.
#
#  Solution: http://thinkpython2.com/code/find_duplicates.py

import os

paths = []

def walk(dirname, suffix):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            if name[-4:] == suffix:
                paths.append(path)
        else:
            walk(path, suffix)
    return paths

# Search dirs and return paths    
path = r'C:\Users\nikda\OneDrive\Documents\Courses\think-python\14. Files\mp3 search'
suffix = '.txt'
walk(path, suffix)

# checksum - check for same contents
checksums = dict()

for filename in paths:
    cmd = 'certutil -hashfile "' + filename + '" MD5'
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    res = res.splitlines()[1]
    checksums.setdefault(res, []).append(filename)

duplicates = []

for checksum, path in checksums.items():
    if len(path) > 1:
        duplicates.append(path)
    
# Double-check with unix command diff - for cmd: FC file1 file2
for paths in duplicates:
    file1 = paths[0]
    file2 = paths[1]
    cmd = 'FC "' + file1 + '" "' + file2 +'"'
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    print(res)    
    

if __name__ == '__main__':
    # ex14_1()
    # ex14_2()
    pass