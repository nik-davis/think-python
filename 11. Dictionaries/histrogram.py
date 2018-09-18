def histogram_verbose(s):
    '''Returns a dictionary with letter:count pairs
    '''
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogram(s):
    '''Histogram using get instead of if statement
    '''
    d = dict()
    for c in s:
        d[c] = d.get(c, 0)
        output = d.get(c, 0)
        d[c] += 1
        print('', c + ':', output, '->', d.get(c, 0))
    return d


def print_hist(h):
    '''Using a dictionary in a for statement traverses the keys of the dictionary,
    but in no particular order.

    Prints each key and corresponding value.
    '''
    for c in h:
        print('', c, h[c])


def print_sorted_hist(h):
    '''Can use sorted function to traverse keys in sorted order.
    '''
    for key in sorted(h):
        print('', key, h[key])


def reverse_loopkup(d, v):
    '''Takes a value and returns the first key that maps to that value.
    Will be slow to use often.
    '''
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()


def invert_dict(d):
    '''Invert a dictionary, from key:values to values:key'''
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            print(' val not in inverse:', key, [key])
            inverse[val] = [key]
            print(' new key', inverse)
        else:
            inverse[val].append(key)
            print(' add to key', inverse)
    return inverse


def invert_dict_setdefault(d):
    '''Taken from exercises; inverst a dictionary using setdefault method
    '''
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


if __name__ == '__main__':
    # In-text exercises and examples
    print('Histogram using get:')
    h = histogram('brontosaurus')
    print(' histogram h =', h)

    print('print_hist:')
    print_hist(h)

    print('Sorted histogram:')
    print_sorted_hist(h)

    hist = histogram_verbose('parrot')
    print('Parrot histogram:', hist)
    inverse = invert_dict(hist)
    print('Parrot inverse:', inverse)

    # Print key and value from highest to lowest frequency
    for key in sorted(inverse, reverse=True):
        print(key, inverse[key])
