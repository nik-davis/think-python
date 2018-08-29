# As an exercise, encapsulate this code in a function named count, and generalize it so that
# it accepts the string and the letter as arguments.
# Then rewrite the function so that instead of traversing the string, it uses the threeparameter
# version of find from the previous section.

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

def count(word, letter):
    '''Counts the appearances of a supplied letter in a supplied word
    using the find function.
    '''
    count = 0
    index = 0

    while index < len(word):
        search = find(word, letter, index)
        if search == -1:
            break
        index = search + 1
        count = count + 1
    print(count)

def count_old(word, letter):
    count = 0
    for l in word:
        if l == letter:
            count = count + 1
    print(count)

count('banana', 'a')