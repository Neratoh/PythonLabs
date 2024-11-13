def full_array():
    array = [[0 for _ in range(7)] for _ in range(7)]
    for i in range(7):
        for j in range(7):
            if i == 0 or i == 6 or j == 0 or j == 6:
                array[i][j] = 1

    for row in array:
        print(' '.join(map(str, row)))

full_array()
