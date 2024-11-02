n = int(input())
formulas = []
for _ in range(n):
    q, r = map(int, input().split())
    formulas.append([q, r])

q = int(input())
for _ in range(q):
    t, d = map(int, input().split())
    formula = formulas[t - 1]
    
    remainder = d % formula[0]
    if remainder <= formula[1]:
        d = d + formula[1] - remainder
    else:
        d = d + formula[0] - remainder + formula[1]
    print(d)
