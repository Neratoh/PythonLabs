def delate(lst, value):
    return [item for item in lst if item != value]

list = input("Введіть елементи списку, розділені пробілом: ").split()
remove = input("Введіть значення, яке потрібно видалити: ")

new_list = delate(list, remove)

print("Новий список після видалення елемента:", new_list)


