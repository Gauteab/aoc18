ops = {
    'addr': lambda a,b,r: r[a] + r[b],
    'addi': lambda a,b,r: r[a] + b,
    'mulr': lambda a,b,r: r[a] * r[b],
    'muli': lambda a,b,r: r[a] * b,
    'banr': lambda a,b,r: r[a] & r[b],
    'bani': lambda a,b,r: r[a] & b,
    'borr': lambda a,b,r: r[a] | r[b],
    'bori': lambda a,b,r: r[a] | b,
    'setr': lambda a,b,r: r[a],
    'seti': lambda a,b,r: a,
    'gtir': lambda a,b,r: 1 if a > r[b] else 0,
    'gtri': lambda a,b,r: 1 if r[a] > b else 0,
    'gtrr': lambda a,b,r: 1 if r[a] > r[b] else 0,
    'eqir': lambda a,b,r: 1 if a == r[b] else 0,
    'eqri': lambda a,b,r: 1 if r[a] == b else 0,
    'eqrr': lambda a,b,r: 1 if r[a] == r[b] else 0
}

def solve_a(r):
    with open('input') as f:
        ip = int(f.readline().split(' ')[1])
        instructions = []
        for line in f:
            s = line.split(' ')
            instructions.append([ops[s[0]]] + [int(x) for x in s[1:]])

    while r[ip] < len(instructions):
        op,a,b,c = instructions[r[ip]]
        r[c] = op(a,b,r)
        r[ip] += 1

    return r[0]

if __name__ == '__main__':
    print(f"Part 1: {solve_a([0] * 6)}")
