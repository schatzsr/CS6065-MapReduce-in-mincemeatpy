#!/usr/bin/env python

"""
Math stats with Mincemeatpy - Given a text file name on the command-line containing one number per line,
print out the sum, count, and standard-deviation of all the numbers in the file.
All statistics should be found in one pass through the data.

Usage:  python mathstats.py small.txt
        python mathstats.py medium.txt
        python mathstats.py large.txt
"""

# Start client with...
# Linux: ./mincemeat.py -l -p changeme
# Windows: python mincemeat.py -l -p changeme

import mincemeat
import sys

textfile = open(sys.argv[1], 'r')

temp = ''
counter = 0
data = []
for l in textfile:
    temp = temp + l
    if counter % 10 == 0:
        data.append(temp)
        temp = ''
    counter = counter + 1
data.append(temp)

textfile.close()

datasource = dict(enumerate(data))


def mapfn(k, v):
    for num in v.split():
        yield 'Sum', int(num)
        yield 'Counter', 1 # Can be anything, since we're just taking the count
        yield 'StdDeviation', float(num)


def reducefn(k, vs):
    if k == 'Sum':
        return sum(vs)
    elif k == 'Counter':
        return len(vs)
    if k == 'StdDeviation':
        avg = sum(vs) / len(vs)
        var = map(lambda x: (x - avg)*(x - avg), vs)
        var_average = sum(var) / len(var)

        import math
        return math.sqrt(var_average)



s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password='changeme')

print ("Count: {}".format(results['Counter']))
print ("Sum: {}".format(results['Sum']))
print ("Std.dev: {}".format(results['StdDeviation']))