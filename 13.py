num = int(input("Введите число:"))
ob = int(input("Введите основание:"))
nb = int(input("Введите новое основание:"))

decimal_num = 0
power = 0
while num > 0:
    decimal_num += (num % 10) * (ob ** power)
    num //= 10
    power += 1

new_num = ""
while decimal_num > 0:
    new_num = str(decimal_num % nb) + new_num
    decimal_num //= nb

print("Число в новой системе счисления:", new_num)