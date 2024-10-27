s = input()
t = input()

result = 0
if s == t:
    print(result)
elif len(s) == len(t):
    for i in range(len(s)):
        if s[i] != t[i]:
            result = i + 1
            break
    print(result)
else:
    min_length = min([len(s), len(t)])
    for i in range(min_length):
        if s[i] != t[i]:
            result = i + 1
            break

    if result == 0:
        result = min_length + 1
    
    print(result)