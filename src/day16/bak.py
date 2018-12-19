

def clear():
    for x in range(0,len(r)):
        r[x] = 0

def addr(a,b,c):
    r[c] = r[a] + r[b]

def addi(a,b,c):
    r[c] = r[a] + b

def mulr(a,b,c):
    r[c] = r[a] * r[b]

def muli(a,b,c):
    r[c] = r[a] * b

def banr(a,b,c):
    r[c] = r[a] & r[b]

def bani(a,b,c):
    r[c] = r[a] & b

def borr(a,b,c):
    r[c] = r[a] | r[b]

def bori(a,b,c):
    r[c] = r[a] | b

def setr(a,b,c):
    r[c] = r[a]

def seti(a,b,c):
    r[c] = a

def gtir(a,b,c):
    r[c] = 1 if a > r[b] else 0

def gtri(a,b,c):
    r[c] = 1 if r[a] > b else 0

def gtrr(a,b,c):
    r[c] = 1 if r[a] > r[b] else 0

def eqir(a,b,c):
    r[c] = 1 if a == r[b] else 0

def eqri(a,b,c):
    r[c] = 1 if r[a] == b else 0

def eqrr(a,b,c):
    r[c] = 1 if r[a] == r[b] else 0

ops   = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

with open('input', 'r') as f:
    i = 0
    m = []
    for line in f:
        if len(line) < 2: continue
        if i == 0 or i == 2:
            m.append(list(map(int, eval(line.split(' ', 1)[1]))))
        else:
            m.append(list(map(int, line.split(' '))))
        i = (i + 1) % 3

def solve_a():
    global r
    count = 0
    for i in range(0, len(m), 3):
        before = m[i]
        inp    = m[i+1]
        after  = m[i+2]
        found = 0
        for op in ops:
            r = before.copy()
            op(inp[1],inp[2],inp[3])
            if r == after:
                if found == 2:
                    count += 1
                    break
                else:
                    found += 1
    print(count)

solve_a()
