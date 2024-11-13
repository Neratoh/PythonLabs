def triangle(N):

    if N <= 1 or N >= 9:
        print("Введіть ціле число в діапазоні 1<N<9")
        return

    for i in range(1, N + 1):
        spaces = ' ' * (N - i)
        stars = '*' * i
        print(spaces + stars)

N = int(input("Введіть ціле число N (1<N<9): "))

triangle(N)



