# Initialise dictionary
eng2cze = dict()

# Assign a list (of strings), a tuple (of strings) and a string to keys
eng2cze['one'] = ['jeden', 'jedna', 'jedno']
eng2cze['two'] = 'dva', 'dvě'
eng2cze['three'] = 'tři'

print(eng2cze)

# Use of 'in' operator; only matches keys
print('one' in eng2cze)
print('jeden' in eng2cze)

# Using values method to fetch values for searching
vals = eng2cze.values()
print('tři' in vals)
print('dva' in vals)

for item in vals:
    print(item)

# Handling different types; this would probably as a basis for search
for item in vals:
    if type(item) == list or type(item) == tuple:
        for word in item:
            print(word)
    else:
        print(item)
