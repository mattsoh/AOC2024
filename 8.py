from itertools import combinations
from math import gcd


def calc(a1, a2, width, height):
    x1, y1 = a1
    x2, y2 = a2
    points = set()
    dx, dy = x2 - x1, y2 - y1
    gcd_val = gcd(dx, dy)
    dx //= gcd_val
    dy //= gcd_val

    x, y = x1 + dx, y1 + dy
    while (x, y) != (x2, y2):
        points.add((x, y))
        x += dx
        y += dy

    for direction in (-1, 1):
        nx, ny = x1 + direction * dx, y1 + direction * dy
        while 0 <= nx < width and 0 <= ny < height:
            points.add((nx, ny))
            nx += direction * dx
            ny += direction * dy

    return points

grid = []
while True:
    try:
        grid.append(input().strip())
    except EOFError:
        break
antennas = {}
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char != '.':
            antennas.setdefault(char, []).append((x, y))

width = len(grid[0])
height = len(grid)
unique = set()
    
for freq, locations in antennas.items():
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            x1, y1 = locations[i]
            x2, y2 = locations[j]

            dx, dy = x2 - x1, y2 - y1

            if dx == 0 or dy == 0:
                continue

            antinode1 = (x1 - dx, y1 - dy)
            antinode2 = (x2 + dx, y2 + dy)

            for antinode in [antinode1, antinode2]:
                ax, ay = antinode
                if 0 <= ax < width and 0 <= ay < height:
                    unique.add(antinode)

print(len(unique))

for freq, locations in antennas.items():
    if len(locations) > 1:
        unique.update(locations)
        for a1, a2 in combinations(locations, 2):
            points = calc(a1, a2, width, height)
            unique.update(points)

print(len(unique))

