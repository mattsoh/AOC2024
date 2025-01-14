from collections import Counter
stone_counts = Counter(map(int,input().split()))
for i in range(9000):
    if (i%100) == 0: print(i)  
    new_stone_counts = Counter()
    for stone, count in stone_counts.items():
        if stone == 0: new_stone_counts[1] += count
        elif len(str(stone)) % 2 == 0:
            new_stone_counts[int(str(stone)[:len(str(stone)) // 2])] += count
            new_stone_counts[int(str(stone)[len(str(stone)) // 2:])] += count
        else:new_stone_counts[stone * 2024] += count
    stone_counts = new_stone_counts
print(sum(new_stone_counts.values()))