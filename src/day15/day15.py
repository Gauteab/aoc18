from sys import argv
from dataclasses import dataclass
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

@dataclass
class Unit:
    id: str
    pos: tuple
    dmg: int = 3
    hp: int = 200

damage = int(argv[2])
def read_input(fname):
    grid = []
    units = {}
    id_count = 0
    with open(fname) as f:
        for y,line in enumerate(f):
            row = []
            for x,c in enumerate(line[:-1]):
                if c == 'E' or c =='G':
                    uid = c + str(id_count)
                    row.append(uid)
                    d = 3 if c=='G' else damage
                    units[uid] = Unit(uid,(x,y),dmg=d)
                    id_count += 1
                else:
                    row.append(c)
            grid.append(row)
    return (grid, units)

grid , units = read_input('input' if len(argv) == 0 else argv[1])
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
    matrix = [[0 if c[0] in 'GE#' else 1 for c in row] for row in grid]
    grid = Grid(matrix=matrix)
    start = grid.node(x1, y1)
    end = grid.node(x2, y2)
    path, _ = AStarFinder().find_path(start, end, grid)
    return path

def reading_order(x,y):
    return [(x,y-1),(x-1,y),(x+1,y),(x,y+1)]

def suroundings(x,y,grid):
    return list(filter(lambda it: grid[it[1]][it[0]] == '.', reading_order(x,y)))

def find_targets(target,grid):
    return [v.pos for k,v in units.items() if k[0] == target]
    #return [(x,y) for y,row in enumerate(grid) for x,c in enumerate(row) if c[0] == target]

def find_in_range(targets, grid):
    in_range = []
    for x, y in targets:
        for x, y in suroundings(x,y,grid):
            in_range.append((x,y))
    return in_range

def shortest(l):
    return min(l, key = lambda x: len(x))

def move(ax, ay, target, grid):

    targets = find_targets(target, grid)
    if not targets: finish()

    in_range = find_in_range(targets, grid)
    if not in_range: return

    reachable = [p for p in [find_path(ax,ay,x,y,grid) for x,y in in_range] if p]
    if not reachable: return

    chosen = shortest(reachable)[-1]
    tx, ty = chosen

    paths = [p for p in [find_path(x,y,tx,ty,grid) for x,y in suroundings(ax,ay,grid)] if p]
    min_path = shortest(paths)

    tx,ty = min_path[0]
    units[grid[ay][ax]].pos = (tx,ty)
    swap(ax,ay,tx,ty,grid)
    return (tx,ty)

class ElfDied(Exception):
    pass

def attack(attacker,target, grid):
    print(attacker)
    target.hp -= attacker.dmg
    if target.hp <= 0:
        x,y = target.pos
        grid[y][x] = '.'
        if target.id[0] == 'E':
            raise ElfDied()
        units.pop(target.id)

def attempt_attack(x,y,target,grid):
    attacker = units[grid[y][x]]
    targets = list(filter(lambda it: grid[it[1]][it[0]][0] == target, reading_order(x,y)))
    if not targets: return False
    targets = [units[grid[y][x]] for x,y in targets]
    target = min(targets, key = lambda t: t.hp)
    attack(attacker,target,grid)
    return True

def do_turn(x,y,grid):
    if not is_unit(grid[y][x]): return
    target = 'E' if grid[y][x][0] == 'G' else 'G'
    if not attempt_attack(x,y,target,grid):
        m = move(x, y, target, grid)
        if m:
            x2,y2 = m
            attempt_attack(x2,y2,target,grid)

def is_unit(s):
    return s[0] == 'E' or s[0] == 'G'

def finish():
    print("Finish!")
    print_grid(grid)
    s = sum([units[x].hp for row in grid for x in row if is_unit(x)])
    print(f"Outcome: {round_c} * {s} = {round_c * s}")
    exit(0)


def main():
    global round_c
    round_c = 0
    while True:
        print(round_c)
        print_grid(grid)
        units_ = [c for row in grid for c in row if is_unit(c)]
        for u in units_:
            if not u in units: continue
            unit = units[u]
            x, y = unit.pos
            do_turn(x,y,grid)
        round_c += 1
try:
    main()
except ElfDied:
    print("Elf died!")
