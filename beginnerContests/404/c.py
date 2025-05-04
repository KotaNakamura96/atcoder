from collections import Counter

n, m = map(int, input().split())

counts = Counter()
result = True

for _ in range(m):
    a, b = map(int, input().split())

    counts[a] += 1
    if counts[a] >= 3:
        result = False
        break

    counts[b] += 1
    if counts[b] >= 3:
        result = False
        break

if not result:
    print("No")
else:
    if counts and all(count == 2 for count in counts.values()):
        print("Yes")
    else:
        print("No")
