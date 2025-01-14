from collections import deque
from collections import defaultdict
def solve(grid):
    rows = len(grid)
    cols = len(grid)
    time = {} # without cheating
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            if grid[r][c] == 'E':
                end = (r, c)
    q = deque([(start, 0, (-1,-1), -1)]) # (position, time)
    cheat = defaultdict(list) # with cheating
    countt = 0
    while q:
        (x,y), dist, (prevx, prevy), cheatdist = q.popleft()
        if countt%1000==0:print(len(q))
        countt += 1
        # print((x,y), dist, (prevx, prevy), cheatdist, len(q))
        if cheatdist == -1: time[(x,y)] = dist
        if (x,y) == end:
            break
        for nx,ny in [(0,1),(0,-1),(1,0),(-1,0)]:
            if nx == -prevx and ny == -prevy:
                continue
            if 0 <= nx+x < rows and 0 <= ny+y < cols:
                if grid[nx+x][ny+y] != '#':
                    if cheatdist == -1:
                        q.append(((x+nx, y+ny), dist+1, (nx, ny), -1))
                    elif cheatdist < 20:
                        cheat[(x+nx, y+ny)].append((dist+1, (x,y)))
                        continue
                    else:
                        continue
                else:
                    if cheatdist == -1:
                        q.append(((x+nx, y+ny), dist+1, (nx, ny), 1))
                    elif cheatdist < 20:
                        q.append(((x+nx, y+ny), dist+1, (nx, ny), cheatdist+1))
                    else:
                        continue
    ways = 0
    for lst in cheat:
        for k in cheat[lst]:
            if time[lst] -k[0] >= 100:
                print(lst, k[0], time[lst], k[1])
                ways +=1
            # else:
                # print(lst, k, time[lst])
    return ways
grid_str = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
# grid_str = """###
# #S.
# ##.
# #E.
# ###"""
grid = [list(row) for row in grid_str.strip().split('\n')]
result = solve(grid)
print(result)