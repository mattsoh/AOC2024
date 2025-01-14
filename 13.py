from sympy import *

x, y = symbols('x y')
total = 0
while True:
    try:
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
    except EOFError:
        break
    c[0] += 10000000000000
    c[1] += 10000000000000
    equations = [Eq(a[0] * x + b[0] * y, c[0]), Eq(a[1] * x + b[1] * y, c[1])]
    solution = linsolve(equations, (x, y))
    for sol in solution:
        if sol[0] % 1 == 0 and sol[1] % 1 == 0:
            total += sol[0] * 3 + sol[1]
    print(solution)

print("Total:", total)