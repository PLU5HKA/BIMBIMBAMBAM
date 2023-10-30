import math
def cgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def clcm(a, b):
    return abs(a * b) // cgcd(a,b)

n = int(input("Введите количество чисел: "))

numbers = []
for i in range(n):
    number = int(input("Введите число: "))
    numbers.append(number)

gcd = numbers[0]
lcm = numbers[0]

for i in range(1, n):
    gcd = cgcd(gcd, numbers[i])
    lcm = clcm(lcm, numbers[i])

print("Наибольший общий делитель (НОД):", gcd)
print("Наименьшее общее кратное (НОК):", lcm)