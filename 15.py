
import sys
from collections import deque
import sys, termios, tty
import os
# Read the original warehouse map and expand it
# original_grid = []
# while True:
#     # try:
#     line = input()
#     if line.strip() == '':
#         break
#     # except EOFError:
#     #     break
#     original_grid.append(line.rstrip('\n'))
original_grid = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########""".split('\n')
# Expand the map
grid = []
for line in original_grid:
    new_line = ''
    for ch in line:
        if ch == '#':
            new_line += '##'
        elif ch == 'O':
            new_line += '[]'
        elif ch == '.':
            new_line += '..'
        elif ch == '@':
            new_line += '@.'
        else:
            new_line += ch * 2
    grid.append(list(new_line))
# moves = input()
for row in grid:
    print(''.join(row))
robot_pos = None
rows = len(grid)
cols = len(grid[0])
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '@':
            robot_pos = (i, j)
            break
    if robot_pos is not None:
        break
dir_map = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
move = "Start"
while True:
    try:
        print(move)
        print(robot_pos[0], robot_pos[1])
        for row in grid:
            print(''.join(row))
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            try:
                move = sys.stdin.read(1)
            except KeyboardInterrupt:
                break
            except EOFError:
                break
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
    except EOFError:
        break
    os.system('clear')
# for move in moves:
    if move not in dir_map:
        continue
    di, dj = dir_map[move]
    ri, rj = robot_pos
    ni, nj = ri + di, rj + dj
    if not (0 <= ni < rows and 0 <= nj < cols):
        continue
    target_cell = grid[ni][nj]
    if target_cell == '.':
        grid[ni][nj] = '@'
        grid[ri][rj] = '.'
        robot_pos = (ni, nj)
    elif target_cell in ['[', ']']:
        if grid[ni][nj] == '[' and nj + 1 < cols and grid[ni][nj + 1] == ']':
            box_cells = [(ni, nj), (ni, nj + 1)]
        elif grid[ni][nj] == ']' and nj - 1 >= 0 and grid[ni][nj - 1] == '[':
            box_cells = [(ni, nj - 1), (ni, nj)]
        else:
            continue
        boxes_to_move = [box_cells]
        queue = deque()
        if dj == -1:
            queue.append((box_cells[0][0] + di, box_cells[0][1] + dj))
        elif dj == 1:
            queue.append((box_cells[1][0] + di, box_cells[1][1] + dj))
        else:
            queue.append((box_cells[0][0] + di, box_cells[0][1] + dj))
            queue.append((box_cells[1][0] + di, box_cells[1][1] + dj))
        not_poss = False
        while queue:
            if not (0 <= ni < rows and 0 <= nj < cols):
                continue
            ci, cj = queue.popleft()
            if grid[ci][cj] == '[' and cj + 1 < cols and grid[ci][cj + 1] == ']':
                box_cells = [(ci, cj), (ci, cj + 1)]
            elif grid[ci][cj] == ']' and cj - 1 >= 0 and grid[ci][cj - 1] == '[':
                box_cells = [(ci, cj - 1), (ci, cj)]
            else:
                if grid[ci][cj] == '#':
                    not_poss = True
                    break
                elif grid[ci][cj] == '.':
                    continue
                else:
                    not_poss = True
                    break
            if box_cells not in boxes_to_move:
                boxes_to_move.append(box_cells)
                # next_i, next_j = ci + di, cj + dj
                if dj == -1:
                    queue.append((box_cells[0][0] + di, box_cells[0][1] + dj))
                elif dj == 1:
                    queue.append((box_cells[1][0] + di, box_cells[1][1] + dj))
                else:
                    queue.append((box_cells[0][0] + di, box_cells[0][1] + dj))
                    queue.append((box_cells[1][0] + di, box_cells[1][1] + dj))
        if not_poss:
            continue
        # print(boxes_to_move)
        # Check if space after last box is empty
        # last_box = boxes_to_move[-1]
        # next_i = last_box[0][0] + di
        # next_j = last_box[0][1] + dj
        # print(next_i, next_j, grid[next_i][next_j], grid[next_i][next_j + 1])
        # print('here')
        # Move boxes
        for box in reversed(boxes_to_move):
            bi1, bj1 = box[0]
            bi2, bj2 = box[1]
            ti1, tj1 = bi1 + di, bj1 + dj
            ti2, tj2 = bi2 + di, bj2 + dj
            if dj == -1:
                grid[ti1][tj1] = grid[bi1][bj1]
                grid[ti2][tj2] = grid[bi2][bj2]
            else:
                grid[ti2][tj2] = grid[bi2][bj2]
                grid[ti1][tj1] = grid[bi1][bj1]
            if (ti1 != bi1 or tj1 != bj1) and (bi1 != ti2 or bj1 != tj2):
                grid[bi1][bj1] = '.'
            if (ti1 != bi2 or tj1 != bj2) and (bi2 != ti2 or bj2 != tj2):
                grid[bi2][bj2] = '.'

        # Move robot
        grid[ni][nj] = '@'
        grid[ri][rj] = '.'
        robot_pos = (ni, nj)
    else:
        continue
total = 0
for i in range(rows):
    j = 0
    while j < cols:
        if grid[i][j] == '[' and j + 1 < cols and grid[i][j + 1] == ']':
            top_dist = i
            left_dist = j
            gps = 100 * top_dist + left_dist
            total += gps
            j += 2
        else:
            j += 1

print(total)