#!/usr/bin/python
checksum = 0

dataset = []

with open('input.tsv') as file:
    for line in file:
        row = [int(x) for x in line.split('\t')]
        checksum += ( max(row) -  min(row) )
        dataset += [row]

print checksum

checksum2 = 0

for row in dataset:
    for i in row:
        for j in row:
            if j == i: continue
            if (i % j == 0):
                checksum2 += ( i / j )

print checksum2
