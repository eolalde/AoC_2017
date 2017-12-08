#!/usr/bin/python

regs = {}
input_file = []
with open('input.txt', 'r') as file:
    for line in file:
        input_file += [line]

def evaluateCondition(x):
    if x[0] not in regs: regs[x[0]] = 0
    if x[1] == '>': return regs[x[0]] > int(x[2])
    if x[1] == '<': return regs[x[0]] < int(x[2])
    if x[1] == '==': return regs[x[0]] == int(x[2])
    if x[1] == '!=': return regs[x[0]] != int(x[2])
    if x[1] == '>=': return regs[x[0]] >= int(x[2])
    if x[1] == '<=': return regs[x[0]] <= int(x[2])
    print 'wtf: {0}'.format(x)

def doOperation(o):
    if o[0] not in regs: regs[o[0]] = 0
    if o[1] == 'inc':
        regs[o[0]] += int(o[2])
    elif o[1] == 'dec':
        regs[o[0]] -= int(o[2])
    return regs[o[0]]

max_reg_value_ever = 0

for line in input_file:
    words = line.split()
    operation = words[:3]
    condition = words[-3:]
    if evaluateCondition(condition):
        result = doOperation(operation)
        if result > max_reg_value_ever:
            max_reg_value_ever = result

max_reg_value = 0

for reg in regs:
    reg_value = regs[reg]
    if reg_value > max_reg_value:
        max_reg_value = reg_value


print regs
print max_reg_value
print max_reg_value_ever
