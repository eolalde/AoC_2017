
input_banks = [0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11]
test_banks = [0,2,7,0]

count = 0
seen = []

current_banks = input_banks[:]
# current_banks = test_banks[:]
while (current_banks not in seen):
    seen += [current_banks[:]]
    # print seen
    blocks_to_flush = max(current_banks)
    bank_to_flush = current_banks.index(blocks_to_flush)
    current_banks[bank_to_flush] = 0

    i = bank_to_flush + 1 if bank_to_flush < len(current_banks) - 1 else 0
    while blocks_to_flush > 0:
        current_banks[i] += 1
        blocks_to_flush -= 1
        i = i + 1 if i < len(current_banks) - 1 else 0

    count += 1


print count

first_seen = seen.index(current_banks)
last_seen = len(seen) - 1

print count - first_seen
