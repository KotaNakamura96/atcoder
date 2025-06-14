n = int(input())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

ans = 0
for i in range(n):
    candidate = min(numbers[i], i + 1)
    ans = max(ans, candidate)

print(ans)