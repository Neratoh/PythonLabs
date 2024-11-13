a = int(input("Введіть значення для a: "))
b = int(input("Введіть значення для b: "))
if a < b:
     result = (a * 3 - 5) / b
elif a == b:
    result =  -4
else:
    result =  (a**4 + b) / a

print("Результат обчислення: ", result)
