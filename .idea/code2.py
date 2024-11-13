numbers = [1, 3, 5, 9, 17]

print(f"{'Число':<10}{'Квадрат':<10}{'Куб':<10}")
print("-" * 30)

for number in numbers:
    square = number ** 2
    cube = number ** 3
    print(f"{number:<10}{square:<10}{cube:<10}")
