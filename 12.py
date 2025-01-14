from collections import defaultdict

m = defaultdict(int)

input_grid = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

for i, line in enumerate(input_grid.splitlines()):
    for j, c in enumerate(line):
        m[(i, j)] = c

notseen = set(m.keys())

ans = 0
ans2 = 0

while notseen:
    start = notseen.pop()
    ch = m[start]
    stack = [start]
    area, perimeter = 0, 0
    sides = set()

    while stack:
        node = stack.pop()
        area += 1
        perimeter += 4

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nxt = (node[0] + dx, node[1] + dy)
            if m[nxt] != ch:
                sides.add((node, (dx, dy)))
                continue
            perimeter -= 1
            if nxt not in notseen:
                continue
            notseen.remove(nxt)
            stack.append(nxt)

    side_adj = 0
    for (node, d) in sides:
        adjacent = (node[0] + d[0], node[1] + d[1])
        if (adjacent, d) in sides:
            side_adj += 1

    ans += area * perimeter
    ans2 += area * (len(sides) - side_adj)

print(ans)
print(ans2)
