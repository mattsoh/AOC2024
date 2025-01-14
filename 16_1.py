from heapq import *
mazer = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
maze = [list(line) for line in mazer.splitlines()]
start, end = None, None
for i,c in enumerate(maze):
    for j,d in enumerate(c):
        if d == 'S':
            start = (i,j)
        elif d == 'E':
            end = (i,j)
pq = []
heappush(pq, (0, start[0], start[1], 0))
vis = set()
while pq:
    cost,i,j, d = heappop(pq)
    if (i, j) == end:
        print(cost)
        break
    if (i, j,d) in vis:
        continue
    vis.add((i, j,d))
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if maze[ni:=i+ dirs[d][0]][nj:=j+dirs[d][1]] != '#':
        heappush(pq,(cost+1, ni, nj, d))
    for nd in [(d +1)% 4,(d -1)%4]:
        heappush(pq,(cost+1000, i, j, nd))  