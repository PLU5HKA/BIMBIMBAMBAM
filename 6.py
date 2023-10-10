import math


def compute_statistics(arr):
    minimum = min(arr)
    maximum = max(arr)
    average = sum(arr) / len(arr)

    squared_diff_sum = sum((x - average) ** 2 for x in arr)
    standard_deviation = math.sqrt(squared_diff_sum / len(arr))

    fifth_central_moment = sum((x - average) ** 5 for x in arr) / len(arr)

    return minimum, maximum, average, standard_deviation, fifth_central_moment


# Пример использования
array = [1, 2, 3, 4, 5]
minimum, maximum, average, standard_deviation, fifth_central_moment = compute_statistics(array)

print("Минимум:", minimum)
print("Максимум:", maximum)
print("Среднее значение:", average)
print("Среднеквадратическое отклонение:", standard_deviation)
print("Пятый центральный момент:", fifth_central_moment)