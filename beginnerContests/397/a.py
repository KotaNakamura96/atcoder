HIGH_FEVER_THRESHOLD = 38.0
MILD_FEVER_THRESHOLD = 37.5

temperature = float(input())

if temperature >= HIGH_FEVER_THRESHOLD:
    print(1)
elif temperature >= MILD_FEVER_THRESHOLD:
    print(2)
else:
    print(3)
