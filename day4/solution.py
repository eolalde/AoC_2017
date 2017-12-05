#!/usr/bin/python

count_1 = 0
count_2 = 0

with open('input.txt', 'r') as file:
    for line in file:
        words = line.split()
        seen = {}
        valid_1 = True
        valid_2 = True
        for i, word in enumerate(words):
            if word not in seen:
                for other_word in seen:
                    other_bag = list(other_word)
                    if len(word) != len(other_word):
                        continue
                    for char in word:
                        if char in other_bag:
                            other_bag.remove(char)
                    if len(other_bag) == 0:
                        valid_2 = False
                seen[word] = 1
            else:
                valid_1 = False
                valid_2 = False

        if valid_1:
            count_1 += 1
        if valid_2:
            count_2 += 1

print count_1
print count_2
