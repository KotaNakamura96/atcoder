height, width, distance = map(int, input().split())

fields = []
for i in range(height):
    fields.append(input())

floors = []
for i in range(height):
    for j in range(width):
        if fields[i][j] == '.':
            floors.append((i, j))

result = 0
for i, (first_height_row, first_heighy_col) in enumerate(floors):
    for (second_height_row, second_height_col) in floors[i+1:]:
        humidifed_floors = set()
        
        for row in range(height):
            for col in range(width):
                if fields[row][col] == '#':
                    continue
                
                first_distance = abs(row - first_height_row) + abs(col - first_heighy_col)
                second_distance = abs(row - second_height_row) + abs(col - second_height_col)
                
                if first_distance <= distance or second_distance <= distance:
                    humidifed_floors.add((row, col))
        
        result = max(result, len(humidifed_floors))

print(result)