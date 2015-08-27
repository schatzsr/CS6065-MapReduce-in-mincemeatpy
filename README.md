MapReduce in mincemeatpy
================

CS6065 Intro to Cloud Computing Homework 3

*Cloned from University of Cincinnati's git site, github.uc.edu*

*Assignment Outline: https://docs.google.com/document/d/1oBZTfU84O6r9HVW_ZbtXiXFEVvRTCrmGdvbEumTio6E/*

#### Usage
*Start client with...*
*Linux:* `./mincemeat.py -l -p changeme`
*Windows:* `python mincemeat.py -l -p changeme`
```
python mathstats.py small.txt
python mathstats.py medium.txt
python mathstats.py large.txt
python freq.py mobydick.txt
python passCrack.py d077f
```

#### Example Output
```
python mathstats.py small.txt
Count: 4
Sum: 131
Std.dev: 27.1235598696

python freq.py mobydick.txt
[ 0.00%  1
] 0.00%  1
$ 0.00%  2
* 0.00%  3
& 0.00%  4
6 0.00%  8
9 0.00%  8
4 0.00%  10
3 0.00%  15
2 0.00%  20
7 0.00%  24
8 0.00%  24
5 0.00%  26
1 0.00%  52
0 0.01%  99
: 0.02%  188
) 0.02%  200
( 0.02%  200
z 0.05%  640
? 0.09%  995
x 0.09%  1006
j 0.09%  1058
q 0.13%  1540
! 0.15%  1743
' 0.24%  2835
" 0.24%  2848
- 0.34%  4012
; 0.35%  4117
. 0.60%  7050
k 0.68%  7925
v 0.72%  8413
b 1.42%  16560
y 1.42%  16569
p 1.44%  16795
, 1.61%  18819
f 1.75%  20424
g 1.75%  20446
w 1.86%  21734
c 1.88%  21964
m 1.96%  22875
u 2.24%  26149
d 3.21%  37583
l 3.59%  41980
r 4.36%  50935
h 5.26%  61543
s 5.39%  62968
i 5.49%  64250
n 5.51%  64430
o 5.82%  68008
a 6.52%  76197
t 7.38%  86240
e 9.81%  114704
  16.51%  193065
  
python passCrack.py d077f
Attacking d077f
{'found': ['cat', 'gkf9']}
```