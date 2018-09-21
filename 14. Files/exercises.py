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


if __name__ == '__main__':
	ex14_1()