def addr(a,b,c,r):
    r[c] = r[a] + r[b]

def addi(a,b,c,r):
    r[c] = r[a] + b

def mulr(a,b,c,r):
    r[c] = r[a] * r[b]

def muli(a,b,c,r):
    r[c] = r[a] * b

def banr(a,b,c,r):
    r[c] = r[a] & r[b]

def bani(a,b,c,r):
    r[c] = r[a] & b

def borr(a,b,c,r):
    r[c] = r[a] | r[b]

def bori(a,b,c,r):
    r[c] = r[a] | b

def setr(a,b,c,r):
    r[c] = r[a]

def seti(a,b,c,r):
    r[c] = a

def gtir(a,b,c,r):
    r[c] = 1 if a > r[b] else 0

def gtri(a,b,c,r):
    r[c] = 1 if r[a] > b else 0

def gtrr(a,b,c,r):
    r[c] = 1 if r[a] > r[b] else 0

def eqir(a,b,c,r):
    r[c] = 1 if a == r[b] else 0

def eqri(a,b,c,r):
    r[c] = 1 if r[a] == b else 0

def eqrr(a,b,c,r):
    r[c] = 1 if r[a] == r[b] else 0

ops   = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

def read_samples():
    samples = []
    with open('samples', 'r') as f:
        i = 0
        for line in f:
            if len(line) < 2: continue
            if i == 0 or i == 2:
                samples.append(list(map(int, eval(line.split(' ', 1)[1]))))
            else:
                samples.append(list(map(int, line.split(' '))))
            i = (i + 1) % 3
    return samples

def solve_a(samples):
    count = 0
    for i in range(0, len(samples), 3):
        before = samples[i]
        inp    = samples[i+1]
        after  = samples[i+2]
        found = 0
        for op in ops:
            r = before.copy()
            op(inp[1],inp[2],inp[3],r)
            if r == after:
                found += 1
                if found == 3:
                    count += 1
                    break
    return count

def solve_b(samples):
    codes = {code:(set(),set()) for code in range(0,16)}
    for i in range(0, len(samples), 3):
        before = samples[i]
        code, a, b, c = samples[i+1]
        after  = samples[i+2]
        for op in ops:
            r = before.copy()
            op(a,b,c,r)
            if r == after:
                codes[code][0].add(op)
            else:
                codes[code][1].add(op)
    codes = {code : sets[0] - sets[1] for code,sets in codes.items()}
    while sum([len(s) for c,s in codes.items()]) > 16:
        sorted_codes = sorted(codes, key = lambda k: len(codes[k]))
        for v in sorted_codes:
            s = codes[v]
            if len(s) > 1: continue
            for code in codes:
                if not code == v:
                    codes[code] -= s
    r = [0] * 4
    with open('program') as f:
        for line in f:
            s = list(map(int, line.split(' ')))
            code,a,b,c = s
            list(codes[code])[0](a,b,c,r)
    return r[0]

if __name__ == '__main__':
    samples = read_samples()
    print(f"Part 1: {solve_a(samples)}")
    print(f"Part 2: {solve_b(samples)}")
