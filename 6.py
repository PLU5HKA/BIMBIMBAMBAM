import math
import scipy

def statistics(arr):
    minimum = min(arr)
    maximum = max(arr)
    average = sum(arr) / len(arr)
    squared_diff_sum = sum((x - average) ** 2 for x in arr)
    standard_deviation = math.sqrt(squared_diff_sum / len(arr))
    fifth_central_moment = scipy.stats.moment(arr, 5)
    # fifth_central_moment = sum((x - average) ** 5 for x in arr) / len(arr)
    averageloc = (minimum + maximum + average + squared_diff_sum + fifth_central_moment)/5
    return minimum, maximum, average, standard_deviation, fifth_central_moment, averageloc

array = [1, 4, 5, 9, 11]
minimum, maximum, average, standard_deviation, fifth_central_moment, averageloc = statistics(array)
print(array)
print("Минимум:", minimum)
print("Максимум:", maximum)
print("Среднее значение:", average)
print("Среднеквадратическое отклонение:", standard_deviation)
print("Пятый центральный момент:", fifth_central_moment)
print("Среднее из вышеуказанных:", averageloc)