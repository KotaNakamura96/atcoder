s = input()
result = 0
position = 0 

for char in s:
    if position % 2 == 0:
        if char == 'o':
            result += 1
        else:
            position += 1
    else:
        if char == 'i':
            result += 1
        else:
            position += 1

if position % 2 != 0:
    result += 1

print(result)
