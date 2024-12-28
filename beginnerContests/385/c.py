n = int(input())
result = 1
buildings = [int(i) for i in input().split()]

heights = {}
for i in range(n):
    h = buildings[i]
    if h not in heights:
        heights[h] = []
    heights[h].append(i)

for positions in heights.values():
    if len(positions) <= result:
        continue
    
    m = len(positions)
    dp = {}
    
    for i in range(m):
        for j in range(i + 1, m):
            distance = positions[j] - positions[i]
            current_key = (j, distance)
            prev_key = (i, distance)
            
            if current_key not in dp:
                if prev_key in dp:
                    dp[current_key] = dp[prev_key] + 1
                else:
                    dp[current_key] = 2
                result = max(result, dp[current_key])

print(result)