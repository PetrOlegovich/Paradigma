def pearson_correlation(x, y):
    if len(x) != len(y):
        raise ValueError("Массивы должны иметь одинаковую длину")

    n = len(x)

    sum_x = sum(x)
    sum_y = sum(y)

    sum_x_squared = sum(x_i ** 2 for x_i in x)
    sum_y_squared = sum(y_i ** 2 for y_i in y)

    sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))

    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2)) ** 0.5

    if denominator == 0:
        return 0

    correlation = numerator / denominator
    return correlation


array1 = [1, 2, 3, 4, 5]
array2 = [2, 3, 4, 5, 6]

correlation = pearson_correlation(array1, array2)
print(f"Коэффициент корреляции Пирсона: {correlation}")