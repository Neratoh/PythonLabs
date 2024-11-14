def every_third_element():
    A = list(map(int, input('Введіть список: ').split()))
    print("Оригінальний спписок:", A)

    result = [A[i] for i in range(2, len(A), 3)]

    print("Список с кожним третім елементом:", result)
    return result

every_third_element()
