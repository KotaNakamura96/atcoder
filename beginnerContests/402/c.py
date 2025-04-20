from collections import defaultdict

n, m = map(int, input().split())

dishes = []
ingredient_to_dishes = defaultdict(list)

for i in range(m):
    ingredients = list(map(int, input().split()))
    k = ingredients[0]
    ingredients = ingredients[1:]
    dishes.append(set(ingredients))
    for j in ingredients:
        ingredient_to_dishes[j].append(i)

overcomings = list(map(int, input().split()))
remaining_ingredients = [len(dish) for dish in dishes]
completed = set()
result = 0

for i in range(n):
    num = overcomings[i]
    completed.add(num)
    
    for j in ingredient_to_dishes[num]:
        remaining_ingredients[j] -= 1
        if remaining_ingredients[j] == 0:
            result += 1
    
    print(result)
