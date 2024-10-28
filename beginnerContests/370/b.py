n = int(input())

elements = []
for i in range(n):
    numbers = [int(i) for i in input().split()]
    elements.append(numbers)

last_element = 1
for i in range(n):
    if last_element >= i + 1:
        last_element = elements[last_element - 1][i]
    elif last_element < i + 1:
        last_element = elements[i][last_element - 1]

print(last_element)