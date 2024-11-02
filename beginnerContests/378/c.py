n = int(input())
numbers = [int(i) for i in input().split()]
result = []

indexes = {}
for index, number in enumerate(numbers):
    if number in indexes:
        result.append(indexes[number])
    else:
        result.append(-1)
    
    indexes[number] = index + 1

print(*result)