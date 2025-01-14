def parse_input(input_map):
    antennas = []
    for y, row in enumerate(input_map):
        for x, char in enumerate(row):
            if char != '.':
                antennas.append((x, y, char))
    return antennas

def calculate_antinodes(antennas, max_x, max_y):
    antinodes = set()
    
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            x1, y1, freq1 = antennas[i]
            x2, y2, freq2 = antennas[j]
            
            if freq1 != freq2:
                continue
            
            dx, dy = x2 - x1, y2 - y1
            
            if dx == 0 or dy == 0:
                continue
            
            antinode1 = (x1 - dx, y1 - dy)
            antinode2 = (x2 + dx, y2 + dy)
            
            for antinode in [antinode1, antinode2]:
                ax, ay = antinode
                if 0 <= ax < max_x and 0 <= ay < max_y:
                    antinodes.add(antinode)
    
    return antinodes
input_map = []
# Example Input
while True:
    a = input()
    if a == "end":
        break
    input_map.append(a)

# Parse input
antennas = parse_input(input_map)
max_x = len(input_map[0])
max_y = len(input_map)

# Calculate antinodes
antinodes = calculate_antinodes(antennas, max_x, max_y)

# Output result
print(f"Unique antinode locations: {len(antinodes)}")
