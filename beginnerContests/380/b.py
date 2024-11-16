s = list(input())

result = []
index = 0
for i in range(len(s)):
    if i == 0:
        continue
    
    if s[i] == '-':
        index += 1
    else:
        result.append(index)
        index = 0

print(*result)
