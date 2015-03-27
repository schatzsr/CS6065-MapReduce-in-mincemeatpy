#!/usr/bin/env python

"""
Letter Frequency with Mincemeatpy - Given a text file name on the command-line containing a text document,
print out the number of times each character is used, along with the percent of the total
with 1 decimal place.  Sort the output so the most seen character is on the bottom.

Usage: python freq.py mobydick.txt
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
    characters = {}
    for character in list(v):
        if character not in characters.keys():
            characters[character] = 1
        else:
            characters[character] = characters[character] + 1

    for key in characters.keys():
        yield 'values', [key, characters[key]]


def reducefn(k, vs):
    sums = 0
    for count in vs:
        sums = sums + count[1]
    result = {}
    for v in vs:
        count = v[1]
        if v[0] not in result.keys():
            percent = round((float(v[1]) / float(sums))* 100, 2)
            result[v[0]] = [count, percent]

        else:
            result[v[0]][0] = result[v[0]][0] + count
            percent = round((float(result[v[0]][0]) / float(sums))* 100, 2)
            result[v[0]][1] = percent

    import operator
    sorted_result = sorted(result.items(), key=lambda (k,v): operator.itemgetter(1)(v))

    return sorted_result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password='changeme')

for r in results['values']:
    print (r[0] + '   ' + str(r[1][1]) + '%' + '   ' + str(r[1][0]))