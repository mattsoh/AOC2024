safe = 0
def b(a, used = False):
    if not used:
        for i in range(len(a)):
            if b(a[:i] + a[i+1:], used = True):
                return True
    if (sorted(a) != a and sorted(a, reverse=True) != a):
        return False
    prev = a[0]-1
    s = True
    for i in a:
        if abs(i - prev) > 3 or i == prev:
            return False
        prev = i
    if s:
        return True
        # print(a)
while True:
    a = input()
    if a == "a":
        break
    a = a.split()
    a = list(map(int, a))
    if (b(a)):
        safe += 1
print(safe)