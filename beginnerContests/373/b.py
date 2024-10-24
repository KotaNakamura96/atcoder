import string
s = input()
alphabets = list(string.ascii_uppercase)

result = 0
last_index = 0
for alpha in alphabets:
    index = s.index(alpha)
    if alpha == 'A':
        last_index = index
        continue

    result = result + (abs(index - last_index))
    last_index = index

print(result)