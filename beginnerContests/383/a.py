n = int(input())
result = 0
last_time = 0
for i in range(n):
    t, v = map(int, input().split())

    if i == 0:
        result += v
        last_time = t
        continue
    
    result -= t - last_time
    if result < 0:
        result = 0

    result += v
    last_time = t

print(result)
