#!/usr/bin/env python

"""
Password cracking with Mincemeatpy - Given a string of characters on the command line,
find what string hashes to it.  Passwords are sometimes stored in a hashed form,
so if the database is breached, the passwords are not easily usable. For this assignment,
assume we have a hash of a password in hex form.  Given this hash on the command line,
find what password hashes to it.  Only the first 5 characters of the hash are checked.
Assume passwords are 4 or fewer characters containing only lowercase letters and numbers.
Use MapReduce to quickly look through all combinations for a match.
Print out the input hash string and the valid passwords which hash to it, if any.
Use hashlib md5 hexdigest()and use the first 5 characters.
Here are some passwords to crack: d077f, 0832c, 1a1dc, ee269, 0fe63

Usage:  python passCrack.py d077f
"""

# Start client with...
# Linux: ./mincemeat.py -l -p changeme
# Windows: python mincemeat.py -l -p changeme

import mincemeat
import sys
import hashlib

hashinput = sys.argv[1]
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

data_dict = {}
for character in data:
    data_dict[character] = hashinput

def mapfn(k, v):
    import hashlib
    fndata = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    m = hashlib.md5(k)
    if m.hexdigest()[:5] == v:
        yield 'Found Match', k
    for a in fndata:
        m = hashlib.md5(k + a)
        if m.hexdigest()[:5] == v:
            yield 'Found Match', k + d
        for b in fndata:
            m = hashlib.md5(k + a + b)
            if m.hexdigest()[:5] == v:
                yield 'Found Match', k + a + b
            for c in fndata:
                m = hashlib.md5(k + a + b + c)
                if m.hexdigest()[:5] == v:
                    yield 'Found Match', k + a + b + c

def reducefn(k, vs):
    return vs

s = mincemeat.Server()
s.datasource = data_dict
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password='changeme')

print ("Attacking {}".format(hashinput))
print (results)