
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

if __name__ == '__main__':
    samples = read_samples()
    print(f"Part 1: {solve_a(samples)}")

