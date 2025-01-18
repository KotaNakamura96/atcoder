x = int(input())

factorials = {2: 2}
current = 2
max = 3 * 10**18
for i in range(3, 21):
    current *= i
    if current > max:
        break
    factorials[current] = i

print(factorials.get(x, -1))
