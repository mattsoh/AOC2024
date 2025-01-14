numk = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '0': (3, 1),
    'A': (3, 2),
    '': (3, 0)
}
numd = {
    '^': (0, 1),
    'v': (1, 1),
    '<': (1, 0),
    '>': (1, 2),
    'A': (0, 2),
    '': (0, 0)
}
move = lambda d: ('^' if d[0] < 0 else 'v', '>' if d[1] > 0 else '<')
@__import__('functools').cache
def calc(pad, instr, vals, pads):
    newval = (numpad:=numk if pad == 0 else numd)[instr[0]]
    dist = (newval[0] - (val:=(vals:=j.loads(vals))[0])[0], newval[1] - val[1])
    final = ([(comm:=('^' if dist[0] < 0 else 'v', '>' if dist[1] > 0 else '<'))[0] * abs(dist[0]) + comm[1] * abs(dist[1]) + 'A'] if list(numpad.keys())[list(numpad.values()).index((newval[0], val[1]))] else [] ) + ([comm[1] * abs(dist[1]) + comm[0] * abs(dist[0]) + 'A']  if list(numpad.keys())[list(numpad.values()).index((val[0], newval[1]))] else [])
    cost, newvals = ([len(f) for f in final], [[] for _ in final]) if pad == pads else ([calc(pad+1, f, j.dumps(vals[1:]), pads)[0] for f in final], [calc(pad+1, f, j.dumps(vals[1:]), pads)[1] for f in final])
    if len(instr) == 1:
        minn = min(zip(cost, newvals))
        return minn[0], [newval] + minn[1]
    else:
        calcc = []
        nextvals = []
        for n in newvals:
            calcans = calc(pad, instr[1:], j.dumps([newval] + n), pads)
            calcc.append(calcans[0])
            nextvals.append(calcans[1])
        minn = min(zip(cost, calcc, nextvals))
        return minn[0] + minn[1], minn[2]
a = 0
c = 0
inp = __import__('sys').stdin.read().splitlines()
for i in range(5):
    b = inp[i]
    intpart = int(b.replace('A',''))
    numpads = [numk['A']] + [numd['A'] for _ in range(25)]
    a+=calc(0, b, (j:=__import__('json')).dumps(numpads[:3]), 2)[0] * intpart
    c+=calc(0, b, j.dumps(numpads[:26]), 25)[0] * intpart
print(a)
print(c)
    
    