from dataclasses import dataclass
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

@dataclass
class Unit:
    id: str
    pos: tuple
    dmg: int = 3
    hp: int = 200
    target: str = ''


def read_input():
    grid = []
    units = {}
    id_count = 0
    with open('input') as f:
        for y,line in enumerate(f):
            row = []
            for x,c in enumerate(line[:-1]):
                if c == 'E' or c =='G':
                    uid = c + str(id_count)
                    row.append(uid)
                    units.update({uid:Unit(uid,(x,y))})
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

def enemies(target,grid):
    return [c for row in grid for c in row if c[0] == target]

def shortest(l):
    f = [x for x in l if x]
    return min(f, key = lambda x: len(x)) if f else None

def move(x, y, target, grid):
    #print(f"x: {x}, y: {y}")
    if not enemies(target,grid):
        finish()
    targets = find_targets(target, grid)
    #print(f"targets: {targets}")
    paths = [find_path(x,y,x2,y2,grid) for x2,y2 in targets]
    #print(f"paths: {paths}")
    if not paths: return
    min_path = shortest(paths)
    if not min_path:
        return
    #print(f"min_path: {min_path}")
    target = min_path[-1]
    x2,y2 = target
    paths = [find_path(x,y,x2,y2,grid) for x,y in suroundings(x,y,grid)]
    #print(f"paths: {paths}")
    min_path = shortest(paths)
    #print(f"min_path: {min_path}")
    x2,y2 = min_path[0]
    units[grid[y][x]].pos = (x2,y2)
    swap(x,y,x2,y2,grid)
    return (x2,y2)

def select_target(x1,y1,target,grid):
    for x,y in reading_order(x1,y1):
        if is_unit(grid[y][x]) and grid[y][x][0] == target:
            return (x,y)

def attack(attacker, target, grid):
    target.hp -= 3
    if target.hp <= 0:
        x,y = target.pos
        grid[y][x] = '.'
        attacker.target = ''

def attempt_attack(x,y,target,grid):
    attacker = units[grid[y][x]]
    if attacker.target:
        t = attacker.target
    else:
        t = select_target(x,y,target,grid)
        if t:
            x,y = t
            t = units[grid[y][x]]
    if t:
        attack(attacker,t,grid)
        return True
    return False

def do_turn(x,y,grid):
    if not is_unit(grid[y][x]): return
    target = 'E' if grid[y][x][0] == 'G' else 'G'
    if not attempt_attack(x,y,target,grid):
        m = move(x, y, target, grid)
        if m:
            x2,y2 = m
            attempt_attack(x2,y2,target,grid)

grid , units = read_input()

def is_unit(s):
    return s[0] == 'E' or s[0] == 'G'

def finish():
    s = sum([units[x].hp for row in grid for x in row if is_unit(x)])
    print(f"Outcome: {round_c} * {s} = {round_c * s}")
    exit(0)

round_c = 0
while True:
    print(round_c)
    print_grid(grid)
    units_ = [(x,y) for y, row in enumerate(grid) for x,c in enumerate(row) if is_unit(c)]
    for x,y in units_:
        do_turn(x,y,grid)
    round_c += 1

