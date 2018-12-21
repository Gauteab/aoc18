from copy import deepcopy
from os import system
from time import sleep

def read_input():
    with open('input') as f:
        grid = []
        for line in f:
            row = []
            for c in line[:-1]:
                row.append(c)
            grid.append(row)
    return grid

def adjacent(x,y,grid):
    adj = []
    if x > 0:
        adj.append(grid[y][x-1])
        if y > 0: adj.append(grid[y-1][x-1])
        if y < len(grid)-1: adj.append(grid[y+1][x-1])
    if x < len(grid[0])-1:
        adj.append(grid[y][x+1])
        if y > 0: adj.append(grid[y-1][x+1])
        if y < len(grid)-1: adj.append(grid[y+1][x+1])
    if y > 0:
        adj.append(grid[y-1][x])
    if y < len(grid)-1:
        adj.append(grid[y+1][x])
    return adj

def print_acres(grid):
    for row in grid:
        print("".join(row))

def resource_value(grid):
    lumber = 0
    wood = 0
    for row in grid:
        for acre in row:
            lumber += 1 if acre == '#' else 0
            wood += 1 if acre == '|' else 0
    return lumber * wood

def render(grid, sleep_t = 0.01):
    sleep(sleep_t)
    system('clear')
    print_acres(grid)

grid = read_input()
buffer = [[0 for x in range(len(grid[0]))] for _ in range(len(grid))]
generations = [deepcopy(grid)]
for gen in range(1,1000):
    for y in range(0,len(grid)):
        for x in range(0,len(grid[y])):
            adj = adjacent(x,y,grid)
            it = grid[y][x]
            if it == '.':
                s = sum(1 for acre in adj if acre == '|')
                buffer[y][x] = '|' if s >= 3 else '.'
            elif it == '|':
                s = sum(1 for acre in adj if acre == '#')
                buffer[y][x] = '#' if s >= 3 else '|'
            elif it == '#':
                lumber = sum(1 for acre in adj if acre == '#')
                trees = sum(1 for acre in adj if acre == '|')
                buffer[y][x] = '#' if lumber >= 1 and trees >= 1 else '.'
    #render(buffer)
    if any(g == buffer for g in generations):
        break
    generations.append(deepcopy(buffer))

    tmp = grid
    grid = buffer
    buffer = tmp

start = [i for i,g in enumerate(generations) if g == buffer][0]
pattern = generations[start:]
iters = 1000000000 - len(generations)

print(f'Part 1: {resource_value(generations[10])}')
print(f'Part 2: {resource_value(pattern[iters % len(pattern)])}')
