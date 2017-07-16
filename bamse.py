#!/usr/bin/python
# This Python file uses the following encoding: utf-8

# bamse.py
__author__ = 'David Lilja'
__version__ = '0.1'

import random

print 'Bamses Honungsjakt\n'

# Antal brickor
brickor = []
for i in range(0,7) :
    brickor.append('vargen')
for i in range(0,32) :
    brickor.append('bamse')
for i in range(0,4) :
    brickor.append('lilleskutt')
for i in range(0,4) :
    brickor.append('farmor')
for i in range(0,4) :
    brickor.append('skalman')
brickor.append('+1')
brickor.append('+2')
brickor.append('+3')

# Slumpa en spelplan
#
# Spelplan kommer att vara den slumpade spelplanen.
# Spelplan2 kommer att vara den spelplan där vargenbrickorna ligger på rad.

min = 1
max = 6

spelplan2 = []
for i in range(0, len(brickor)) :
    spelplan2.append(brickor[i-1])

spelplan = []
for i in range(0,len(brickor)) :
    bricka = random.randint(min, len(brickor))
    spelplan.append(brickor[bricka-1])
    del brickor[bricka-1]

# Slumpa ett spel på spelplanen
spel = 1000000
blandat = 0
totalvarg = 0.0
totalvarg7 = 0.0

for spel in range(0,spel+1) :
    steg = 0
    vargen = 0
    vargen2 = 0
    while steg < len(spelplan2) :
        tarning = random.randint(min, max)
        steg = steg + tarning
        if steg + tarning > 51 :
            break
        if spelplan[steg-1] == 'vargen' :
            vargen += 1
        if spelplan2[steg-1] == 'vargen' :
            vargen2 += 1

    totalvarg = totalvarg + vargen
    totalvarg7 = totalvarg7 + vargen2

print 'Den slumpade spelplanen blev såhär:'
print spelplan, '\n'
print 'Antal omgångar spelade på spelplanen:', spel
print 'Hur många vargar på slumpade planen?:', totalvarg/spel
print 'Hur många vargar på 7-iradplanen?   :', totalvarg7/spel
