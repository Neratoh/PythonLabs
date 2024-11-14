def calculate_expression(x, y):
    if x > 8:
        return 3 + y
    else:
        return 9 * x * y

def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

x = int(input("Введіть значення x:"))
y = int(input("Введіть значення y:"))
print ("Результат = ", calculate_expression(x, y))

n = int(input("Введіть значення"))
print("Факторіал = ", calculate_factorial(n))