def find_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    count = 0

    def check_direction(x, y, dx, dy):
        for i in range(word_len):
            if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] != word[i]:
                return False
            x += dx
            y += dy
        return True

    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1),  # right, down, down-right, down-left
        (0, -1), (-1, 0), (-1, -1), (-1, 1)  # left, up, up-left, up-right
    ]

    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if check_direction(r, c, dx, dy):
                    count += 1

    return count

# Example usage
grid = []
while True:
    a = input()
    if a == "dd":
        break
    grid.append(list(a))

word = "XMAS"
# print(find_word(grid, word))  # Output: 18
count = 0
for i in range(len(grid)-2):
    for j in range(len(grid[i])-2):
            if( (grid[i][j] == 'M' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'S')\
                or (grid[i][j] == 'S' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'M'))\
                and(( grid[i+2][j] == 'M' and grid[i][j+2] == 'S') or (grid[i+2][j] == 'S' and grid[i][j+2] == 'M')):
                    count += 1
print(count)