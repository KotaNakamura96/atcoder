q = int(input())

queues = []
result = []
for i in range(q):
    inputs = input().split()
    if inputs[0] == '1':
        card = inputs[1]
        queues.append(int(card))
    else:
        target = queues.pop(0)
        result.append(target)

for num in result:
    print(num)
