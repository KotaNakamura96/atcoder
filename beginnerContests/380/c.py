n, k = map(int, input().split())
s = list(input())

blocks = []
start_block_index = 0
block_index = 0
target_last_index = 0
current = 0
for i in range(n):
    if i == 0 and s[i] == '1':
        block_index += 1
        current = 1
        continue

    if i + 1 == n:
        if start_block_index == 0:
            start_block_index = i

        blocks = s[start_block_index:i+1]
        for j in range(len(blocks)):
            s[target_last_index + j], s[start_block_index + j] = s[start_block_index + j], s[target_last_index + j]

        break
    
    if s[i] == '1':
        if current == 1:
            continue

        block_index += 1
        current = 1

        if block_index == k:
            start_block_index = i

    if s[i] == '0':
        if current == 0:
            continue
        
        current = 0
        if block_index == k - 1 and target_last_index == 0:
            target_last_index = i

        if block_index == k:
            blocks = s[start_block_index:i]

            for j in range(len(blocks)):
                s[target_last_index + j], s[start_block_index + j] = s[start_block_index + j], s[target_last_index + j]

            break

print(''.join(s))
