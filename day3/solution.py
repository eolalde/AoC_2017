#!/usr/bin/python

def solution(input, solution):
    if input == 1: return 0, 2

    last_sum = 1
    half_side = 1
    direction = 'U'

    grid = {
        (0,0): 1,
        (1,0): 1
    }

    x, y = ( 1, 0 )
    for i in range(2, input + 1):
        # print (x, y)
        if input == i and solution == 1:
            return ( abs(x) + abs (y) )
        elif last_sum > input and solution == 2:
            return last_sum
        if direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        elif direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1

        last_sum = getSum(x, y, grid)
        grid[x, y] = last_sum

        if x == half_side and y == half_side:
            direction = 'L'
        elif x == -half_side and y == half_side:
            direction = 'D'
        elif x == -half_side and y == -half_side:
            direction = 'R'
        elif x == half_side + 1 and y == -half_side:
            direction = 'U'
            half_side += 1
    

def getSum(x, y, grid):
    SUM = 0
    if (x+1, y) in grid:
        SUM += grid[x+1, y]
    if (x+1, y+1) in grid:
        SUM += grid[x+1, y+1]
    if (x, y+1) in grid:
        SUM += grid[x, y+1]
    if (x-1, y) in grid:
        SUM += grid[x-1, y]
    if (x, y-1) in grid:
        SUM += grid[x, y-1]
    if (x-1, y-1) in grid:
        SUM += grid[x-1, y-1]
    if (x-1, y+1) in grid:
        SUM += grid[x-1, y+1]
    if (x+1, y-1) in grid:
        SUM += grid[x+1, y-1]
    # print SUM
    return SUM

input = 325489
# input = 23

print solution(input, 1)
print solution(input, 2)