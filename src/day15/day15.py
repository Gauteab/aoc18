from dataclasses import dataclass
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

@dataclass
class Unit:
    id: str
    dmg: int = 3
    hp: int = 200
    target: str = ''


def read_input():
    grid = []
    units = {}
    id_count = 0
    with open('input') as f:
        for line in f:
            row = []
            for c in line[:-1]:
                if c == 'E' or c =='G':
                    uid = c + str(id_count)
                    row.append(uid)
                    units.update({uid:Unit(uid)})
                    id_count += 1
                else:
                    row.append(c)
            grid.append(row)
    return (grid, units)

def print_grid(grid):
    for row in grid:
        for c in row:
            print(c if c == '#' or c == '.' else c[0], end='')
        print()

def swap(x1, y1, x2, y2, grid):
    tmp = grid[y1][x1]
    grid[y1][x1] = grid[y2][x2]
    grid[y2][x2] = tmp

def print_matrix(matrix):
    for row in matrix:
        for c in row:
            print(c, end="")
        print()

def find_path(x1,y1,x2,y2,grid):
    matrix = [[0 if c[0] in ['G','E','#'] else 1 for c in row] for row in grid]
    grid = Grid(matrix=matrix)
    start = grid.node(x1, y1)
    end = grid.node(x2, y2)
    path, _ = AStarFinder().find_path(start, end, grid)
    return path

def reading_order(x,y):
    return [(x,y-1),(x-1,y),(x+1,y),(x,y+1)]

def suroundings(x,y,grid):
    return list(filter(lambda it: grid[it[1]][it[0]] == '.', reading_order(x,y)))

def find_targets(target, grid):
    targets = [] # List of (x,y)
    for y,row in enumerate(grid):
        for x,c in enumerate(row):
            if not is_unit(c): continue
            if c[0] == target:
                for x,y in suroundings(x,y,grid):
                    targets.append((x,y))
    return targets

def shortest(l):
    return min(l, key = lambda x: len(x))

def move(x, y, target, grid):
    print(f"x: {x}, y: {y}")
    targets = find_targets(target, grid)
    print(targets)
    paths = [find_path(x,y,x2,y2,grid) for x2,y2 in targets]
    print(paths)
    if not paths: return
    min_path = shortest(paths)
    print(min_path)
    target = min_path[-1]
    x2,y2 = target
    paths = [find_path(x,y,x2,y2,grid) for x,y in suroundings(x,y,grid)]
    min_path = shortest(paths)
    x2,y2 = min_path[0]
    swap(x,y,x2,y2,grid)

def select_target(x1,y1,target,grid):
    for x,y in reading_order(x1,y1):
        if is_unit(grid[y][x]) and grid[y][x][0] == target:
            return (x,y)

def do_turn(x,y,grid):
    unit = grid[y][x]
    if not is_unit(unit): return
    target = 'E' if grid[y][x][0] == 'G' else 'G'
    t = select_target(x,y,target,grid)
    if t:
        return
    move(x, y, target, grid)

grid , units= read_input()

def is_unit(s):
    return s[0] == 'E' or s[0] == 'G'

while True:
    print_grid(grid)
    units_ = [(x,y) for y, row in enumerate(grid) for x,c in enumerate(row) if is_unit(c)]
    input()
    for x,y in units_:
        do_turn(x,y,grid)

