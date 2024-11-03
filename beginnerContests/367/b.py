whole_number, decimal_number = input().split('.')

while decimal_number and int(decimal_number[-1]) == 0:
    decimal_number = decimal_number[:-1]

if decimal_number:
    print(whole_number + '.' + decimal_number)
else:
    print(whole_number)

