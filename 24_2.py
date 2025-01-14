from collections import defaultdict
import graphviz
import sys
text = sys.stdin.read()
chunks = text.strip().split('\n\n')

lwires, lgates = chunks
wires = {}
for line in lwires.strip().splitlines():
    k, v = line.split(': ')
    v = int(v)
    wires[k] = v

gates = {}
for line in lgates.strip().splitlines():
    in_, out = line.split(' -> ')
    in_ = in_.split()

    assert out not in gates
    gates[out] = in_


def match_against(out, spec):
    if spec == '*':
        return set()

    if out in gates:
        in_ = gates.get(out)
        a, op, b = in_
    else:
        if spec == out:
            return set()
        return {out}

    if spec[0] != op:
        return {out}

    e_ab = match_against(a, spec[1]) | match_against(b, spec[2])
    e_ba = match_against(b, spec[1]) | match_against(a, spec[2])
    e = min(e_ab, e_ba, key=len)
    return e


zs = [k for k in gates.keys() if k.startswith('z')]
es = set()
for z in zs:
    n = int(z[1:])
    prev = n-1
    x_this = z.replace('z', 'x')
    y_this = z.replace('z', 'y')

    x_prev = f'x{prev:02d}'
    y_prev = f'y{prev:02d}'

    es |= match_against(
        z,
        ['XOR',
           ['XOR', x_this, y_this],
           ['OR', ['AND', x_prev, y_prev],
                  ['AND', ['XOR', x_prev, y_prev],
                          '*']]])

g = defaultdict(list)
for out, in_ in gates.items():
    a, op, b = in_
    n = f'{a} {op} {b}'
    g[a].append(n)
    g[b].append(n)
    g[n].append(out)
# print(es)
dot = graphviz.Digraph()
for src, edges in g.items():
    for edge in edges:
        color = 'red' if edge in es else 'black'
        dot.edge(src, edge, color=color)
        # dot.node(edge, color='red')
dot.render("gates_graph.gv", view=True)