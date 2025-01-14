import re
import time
import os

# Grid dimensions
width = 101
height = 103
seconds = 100

robots = []

# Read input
with open('input.txt') as f:
    for line in f:
        m = re.match(r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)', line.strip())
        if m:
            x, y, vx, vy = map(int, m.groups())
            robots.append({'x': x, 'y': y, 'vx': vx, 'vy': vy})

# Simulate motion
for i in range(999999999999):
    grid = [[0 for _ in range(width+100)] for _ in range(height+100)]
    bad = True
    os.system('cls' if os.name == 'nt' else 'clear')
    for robot in robots:
        robot['x'] = (robot['x'] + robot['vx']) % width
        robot['y'] = (robot['y'] + robot['vy']) % height
        grid[robot['y']][robot['x']] += 1
        if (grid[robot['y']][robot['x']] > 1):
            bad = False
    # Print 2D grid
    # if bad and i > 0:
    grid1 = [[' ' for _ in range(width)] for _ in range(height)]
    for robot in robots:
        grid1[robot['y']][robot['x']] = '#'

    for row in grid1:
        print(''.join(row))
    print(i)
    time.sleep(0.01)
# Center lines
center_x = width // 2
center_y = height // 2
quadrants = [0, 0, 0, 0]  # Q1, Q2, Q3, Q4

# Count robots in each quadrant
for robot in robots:
    x, y = robot['x'], robot['y']
    if x == center_x or y == center_y:
        continue  # Exclude robots on center lines
    if x > center_x and y < center_y:
        quadrants[0] += 1  # Q1
    elif x < center_x and y < center_y:
        quadrants[1] += 1  # Q2
    elif x < center_x and y > center_y:
        quadrants[2] += 1  # Q3
    elif x > center_x and y > center_y:
        quadrants[3] += 1  # Q4

# Calculate safety factor
print(quadrants)
safety_factor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
print(safety_factor)