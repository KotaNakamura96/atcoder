def exists_target_inline(lines):
    for line in list(lines):
        if line == '#':
            return True
        
    return False

field_lines = []
for i in range(8):
    s = input()
    field_lines.append(s)

replaces_line_fields = []
for field_line in field_lines:
    if exists_target_inline(field_line):
        # continue
        replaced_field_line = field_line.replace('.', '#')
        replaces_line_fields.append(replaced_field_line)
    else:
        replaces_line_fields.append(field_line)

field_rows = []
for i in range(8):
    row = ''
    for j in range(8):
        row += field_lines[j][i]

    field_rows.append(row)

replaces_row_fields = []
for field_row in field_rows:
    if exists_target_inline(field_row):
        # continue
        replaced_field_row = field_row.replace('.', '#')
        replaces_row_fields.append(replaced_field_row)
    else:
        replaces_row_fields.append(field_row)

result = 0
for i in range(8):
    for j in range(8):
        if replaces_line_fields[i][j] == '.' and replaces_row_fields[j][i] == '.':
            result += 1

print(result)
