n = int(input())
races = list(map(int, input().split()))
k = int(input())

result = 0
for i in range(len(races)):
    if races[i] >= k:
        result += 1

print(result)
