# Open a file for writing. If exists, deletes contents, if not, creates.
fout = open('14. Files/output.txt', 'w')

line1 = 'open returns a file object that provides methods for working with the file.\n'
line2 = 'The write method puts data into the file.\n'

fout.write(line1)
fout.write(line2)

line3 = 'File object keeps track of position, so if call write again, adds to end\n'

return_value = fout.write(line3)

print('Return value of write is number of chars written:', return_value)

# The arg of write has to be string, must convert other values
x = 42
fout.write(str(x))

# Or use format operator
fout.write('\nIn %g years I have spotted %d %s\n' % (2.5, 3, 'camels'))

# When done writing, should close the file
fout.close()


# Files organised into directories (folders).
import os
cwd = os.getcwd()
print('Current working directory:', cwd)
print('Relative path:', os.path.relpath('output.txt'))
print('Absolute path:', os.path.abspath('output.txt'))

print(os.path.exists('path'), os.path.isdir('path'), os.listdir('14. Files'))

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

print('Walk:')
walk('14. Files')

# Walk using os.walk
for root, dirs, files in os.walk('14. Files'):
    for filename in files:
        print(os.path.join(root, filename))
    

# Catching exceptions
try:
    fin = open('not_a_file.txt')
except:
    print('Caught an exception!')


# Databases: Organised like dictionaries
import dbm

db = dbm.open('14. Files/locations', 'c') # 'c' created if doesn't exist
db['cat'] = 'Hiding under the bed'
print('bytes object:', db['cat'])

for key in db:
    print('Iteration:', key, db[key])

db.close()

# Pickling: keys and values for dbm have to be strings or bytes
import pickle

t = [1, 2, 3]
s = pickle.dumps(t)
print('Pickle dump string:', t, '->', s)
t2 = pickle.loads(s)
print('Pickle load string:', s, '->', t2)

# Pickling then unpickling has same effect as copying object
# For database storage, module: shelve

# Pipes
cmd = 'dir'
fp = os.popen(cmd)
res = fp.read()
print(res)
stat = fp.close()
print('Final status of process. None means ended normally:', stat)

# Checksum
#certutil -hashfile followed by the file name and then MD5.
filename = '"14. Files/output.txt"'
cmd = 'certutil -hashfile ' + filename + ' MD5'
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(res)
print(stat)

# Debugging strings and whitespace
s = '1 2\t 3\n 4'
print(s)
print(repr(s)) # String representation of object