k = int(input())
s = input()
t = input()

result = 'No'
if s == t:
    result = 'Yes'
else:
    s_len = len(s)
    t_len = len(t)

    if abs(s_len - t_len) >= 2:
        result = 'No'
    elif s_len == t_len:
        duplicated_count = 0
        for i in range(s_len):
            if s[i] == t[i]:
                duplicated_count += 1

        if s_len - 1 == duplicated_count:
            result = 'Yes'
    else: # 長さは1文字違いのケース
        if t_len < s_len:
            t_index = 0
            duplicated_count = 0
            for i in range(s_len):
                if t_index < t_len and s[i] == t[t_index]:
                    t_index += 1
                    duplicated_count += 1

            if s_len - 1 == duplicated_count:
                result = 'Yes'
        else: # s_len < t_len:
            s_index = 0
            duplicated_count = 0
            for i in range(t_len):
                if s_index < s_len and s[s_index] == t[i]:
                    s_index += 1
                    duplicated_count += 1
            if t_len - 1 == duplicated_count:
                result = 'Yes'

print(result)