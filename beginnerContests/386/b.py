s = input()
result = ''
count = 0
i = 0
is_zero = False

while i < len(s):
    if i == 0:
        result += s[i]
        count += 1
        i += 1
        continue
        
    if s[i] == '0':
        if is_zero:
            result += '00'
            is_zero = False
            count += 1
            i += 1
        else:
            if i == len(s) - 1:
                result += '0'
                count += 1
                i += 1
            else:
                if s[i + 1] == '0':
                    is_zero = True
                    i += 1
                else:
                    result += '0'
                    count += 1
                    i += 1
    else:
        result += s[i]
        count += 1
        i += 1
        is_zero = False

print(count)