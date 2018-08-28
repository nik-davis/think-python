string = 'hello world'

# First letter capitalised, rest lowercase
new_string = string.capitalize()
print('Capitalize:', string, '->', new_string)

# Similar to lowercasing but more aggressive, intended to remove all
# case distinctions
string = 'Hello WORLDß'
case_fold = string.casefold()
print('Casefold:', string, case_fold)

# Returns centered string of length 'width'. Optional: specify fillchar
# Returns original string if width < len(string)
string = 'Hello world!'
center = string.center(20, '-')
print('Center: ', '|' + center + '|')

# Count non-overlapping occurrences of substring in optional [start, end] range
string = 'Hello hello world'
count = string.count('ello', 0, 12)
print('Count:', count)

# Encode
string = 'Hello world'
encoded = string.encode(encoding="utf-8", errors="strict")

# endswith(suffix[, start[, end]])
string = 'Hello World'
ends = string.endswith('or', 0, -2)
print('Endswith:', ends)
# startswith(prefix[, start[, end]]) 




# expandtabs(tabsize=8)
string = 'Hello\tbig\twide\tworld\t'
expand = string.expandtabs(12)
print('ExpandTabs:', string, '|', expand)

# find(sub[, start[, end]]) return lowest index in string (-1 if not found)
# Only use if need to know position, otherwise use 'in' operator
string = 'Hello World'
find = string.find('ello', 0, -1)
print('Find:', find, 'ello' in string)

# format(*args, **kwargs) literal text or replacement fields using {}
# Each {} contains numerical index or name of a keyword argument
num1 = 1
num2 = 2
print('The sum of {0} + {1} is {sum}'.format(num1, num2, sum=(num1+num2)))

# format_map(mapping)

# index(sub[, start[, end]]) Like find() but raise ValueError when substr not found
string = 'Hello World'
index = string.index('ello', 0, -1)
print('Index:', index)

# isalnum() returns True if all chars alphanumeric and at least one character
print('islanum: ', 'hello'.isalnum(), '123'.isalnum(), 'hi 1'.isalnum(), ''.isalnum())

# isalpha() all alphabetic (all 'letters')
# isascii() 
# isdecimal()
# isdigit()
# isidentifier()
# islower()
# isnumeric()
# isprintable()
# isspace()
# istitle()
# isupper()

# join(iterable)
print('Join:', 'hello'.join('-=-'))

# ljust(width[, fillchar]) left justify

# lower() all cased characters converted to lowercase

# maketrans(x[, y[, z]]) returns translation table usable for str.translate()

# partition(sep) split at first sep, return 3-tuple of before, sep, after
print('partition'.partition('tit'))

# replace(old, new[, count])
old_string = 'Python is boring boring boring!'
new_string = old_string.replace('boring', 'fun')
print('Replace:', new_string)

# rfind(sub[, start[, end]]) return highest index, -1 if sub not found
print('rfind:', 'heeey'.rfind('e'))

# rindix(sub[, start[, end]]) like rfind but raises ValueError if sub not found

# rjust(width[, fillchar]) right justified
print('Right Justified:', 'Over Here!'.rjust(150))

# rpartition(sep) split at last occurrence of sep. If not found, two empty strings then string itself

# split(sep=None, maxsplit=-1) Return list of words in string using sep as delimiter
print('lots and lots of words'.split())
print('whitespace    handling'.split(' '))
print('and<>other<>chars'.split('<>'))
# rsplit(sep=None, maxsplit=-1) splits from the right (noticable when maxsplit defined)
# splitlines([keepends]) list of lines in string, breaking at line boundaries

# strip([chars]) leading and trailing chars removed
print('//------stripped------//'.strip('-/'))
# lstrip([chars]) defaults to whitespace, all leading chars removed
print('   lstrip:'.lstrip(), 'www.github.com'.lstrip('w.com'))
# rstrip([chars]) trailing characters removed

# swapcase() upper to lower and lower to upper
print('tHIS WOULD OTHERWISE BE ANNOYING'.swapcase())

# title() titlecases string, first char upper and rest lower
print('this hAs bEEn TITLeified'.title())

# translate()

# upper() all cased characters converted to uppercase
print('shouting'.upper())

# zfill(width)