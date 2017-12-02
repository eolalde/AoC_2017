
checksum = 0

dataset = []

with open('input.tsv') as file:
    for line in file:
        smallest, largest = ( 0, 0 )
        row = line.split('\t')
        rowNumbers = [int(x) for x in row]
        dataset += [rowNumbers]
        for x in rowNumbers:
            if x < smallest or smallest == 0:
                smallest = x
            if x > largest or largest == 0:
                largest = x
        checksum += (largest - smallest)

print checksum

print dataset

checksum2 = 0

for row in dataset:
    for i in row:
        for j in row:
            if j == i: continue
            if (i % j == 0):
                checksum2 += ( i / j )

print checksum2
