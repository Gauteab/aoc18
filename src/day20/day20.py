from collections import deque
from collections import namedtuple

class Pos(namedtuple('Pos','x y')):

    def __new__(cls, x, y):
        return super(Pos, cls).__new__(cls, x, y)

    def __add__(self,other):
        return Pos(self.x + other.x, self.y + other.y)

def transform_input(c):
    if c in '(|)': return c
    if   c == 'E': return Pos(-1, 0)
    elif c == 'W': return Pos( 1, 0)
    elif c == 'N': return Pos( 0,-1)
    elif c == 'S': return Pos( 0, 1)

def read_input():
    inputs = (transform_input(c) for c in open('input').readline()[1:-2])
    data = []
    buffer = []
    for i in inputs:
        if isinstance(i,str):
            if buffer:
                data.append(buffer)
                buffer = []
            data.append(i)
        else:
            buffer.append(i)
    if buffer:
        data.append(buffer)
    return data

data = read_input()
step_len = 0
pos = Pos(0,0)
len_stack = deque([])
pos_stack = deque([])
seen = {}

for i in data:
    if   i == '(':
        len_stack.append(step_len)
        pos_stack.append(pos)
    elif i == ')':
        step_len = len_stack.pop()
        pos = pos_stack.pop()
    elif i == '|':
        step_len = len_stack[-1]
        pos = pos_stack[-1]
    else:
        for step in i:
            step_len += 1
            pos += step
            if not pos in seen:
                seen[pos] = set([step_len])
            else:
                seen[pos].add(step_len)

shortest_paths = [ (pos, min(seen[pos])) for pos in seen ]
part1 = max(shortest_paths, key = lambda p: p[1])[1]
part2 = sum(1 for x in shortest_paths if x[1] >= 1000)
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
