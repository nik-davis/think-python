# In-text exercises and examples

def histogram(s):
    '''Returns a dictionary with letter:count pairs
    '''
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogram_concise(s):
    '''Histogram using get instead of if statement
    '''
    d = dict()
    for c in s:
        d[c] = d.get(c, 0)
        output = d.get(c, 0)
        d[c] += 1
        print(c + ':', output, '->', d.get(c, 0))
    return d

h = histogram_concise('brontosaurus')
print('histogram h =', h)

for c in h:
    print(c, h[c])

def invert_dict(d):
    '''Invert a dictionary, from key:values to values:key'''
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            print('here:', key, [key])
            inverse[val] = [key]
            print('new key', inverse)
        else:
            inverse[val].append(key)
            print('add to key', inverse)
    return inverse

hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse)