n, k = map(int, input().split())
s = list(input())

result = 0
adjacent_healthy_teeth = 0
for i in range(len(s)):
    if s[i] == 'O':
        adjacent_healthy_teeth += 1
    else:
        adjacent_healthy_teeth = 0
    
    if adjacent_healthy_teeth == k:
        result += 1
        adjacent_healthy_teeth = 0
        for j in range(k):
            s[i - k + (j + 1)] = 'X'
        
print(result)