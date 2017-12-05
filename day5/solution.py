#!/usr/bin/python

jumps = []

with open('input.txt', 'r') as file:
    for jump in file:
        jumps += [int(jump)]

jump_count = 0
index = 0
jumps2 = jumps[:]

while True:
    jump_count += 1

    next_index = index + jumps[index]
    jumps[index] += 1

    if next_index >= len(jumps):
        break
    else:
        index = next_index

print jump_count

jump_count2 = 0
index = 0
while True:
    jump_count2 += 1

    next_index = index + jumps2[index]
    if jumps2[index] >= 3:
        jumps2[index] -= 1
    else:
        jumps2[index] += 1

    if next_index >= len(jumps2):
        break
    else:
        index = next_index

print jump_count2