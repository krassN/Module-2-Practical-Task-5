def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        list_1 = []
        for j in range(m):
            list_1.append(value)
        matrix.append(list_1)

    return matrix


result_1 = get_matrix(2, 2, 10)
result_2 = get_matrix(3, 5, 42)
result_3 = get_matrix(4, 2, 13)
print(result_1)
print(result_2)
print(result_3)
