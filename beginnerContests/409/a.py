n = int(input())
t = input()
a = input()

result = False

for i in range(n):
    if t[i] == 'o' and a[i] == 'o':
        result = True
    

if result:
    print('Yes')
else:
    print('No')