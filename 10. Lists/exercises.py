#                                                                      #
# -----------------------Chapter 10: Lists---------------------------- #
#                                                                      #

# 10.1. Write a function called nested_sum that takes a list of lists of 
# integers and adds up the elements from all of the nested lists. For example: 
# 
# >>> t = [[1, 2], [3], [4, 5, 6]] 
# >>> nested_sum(t) 
# 21 

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
    '''Write a function called nested_sum that takes a list of lists of 
    integers and adds up the elements from all of the nested lists.
    '''
    t = [[1, 2], [3], [4, 5, 6]]
    nested_sum(t)

# 10.2 Write a function called cumsum that takes a list of numbers and 
# returns the cumulative sum; that is, a new list where the ith element 
# is the sum of the first i + 1 elements from the original list. For example: 
# 
# >>> t = [1, 2, 3] 
# >>> cumsum(t) 
# [1, 3, 6] 

def cumsum(t):
    '''
    t: List
    '''
    s = []
    s += [t[0]]
    # s[1] = s[0] + t[1]
    # s[2] = s[1] + t[2]

    for i in range(len(t)):
        pass

    print(s)

cumsum([1, 2, 3])

# Run solutions
# ex10_1()
