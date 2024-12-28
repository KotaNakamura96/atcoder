h, w, x, y = map(int, input().split())
fields = []
for i in range(h):
    s = input()
    fields.append(s)

t = input()
x, y = x - 1, y - 1
passed_house_count = 0
passed_x_y = set()
for i in range(len(t)):
    if t[i] == 'U' and x - 1 >= 0 and fields[x - 1][y] != '#':
        if fields[x-1][y] == '@' and (x - 1, y) not in passed_x_y:
            passed_house_count += 1
            passed_x_y.add((x-1, y))
        x, y = x - 1, y
    elif t[i] == 'D' and x + 1 < h and fields[x + 1][y] != '#':
        if fields[x + 1][y] == '@' and (x + 1, y) not in passed_x_y:
            passed_house_count += 1
            passed_x_y.add((x+1, y))
        x, y = x + 1, y
    elif t[i] == 'L' and y - 1 >= 0 and fields[x][y - 1] != '#':
        if fields[x][y - 1] == '@' and (x, y - 1) not in passed_x_y:
            passed_house_count += 1
            passed_x_y.add((x, y - 1))
        x, y = x, y - 1
    elif t[i] == 'R' and y + 1 < w and fields[x][y + 1] != '#':
        if fields[x][y + 1] == '@' and (x, y + 1) not in passed_x_y:
            passed_house_count += 1
            passed_x_y.add((x, y + 1))
        x, y = x, y + 1
print(x + 1, y + 1, passed_house_count)