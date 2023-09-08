# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 50 -> 1, 2, 4, 8, 16, 32

N = int(input("Введите число : "))

power_of_two = 1
result = []

while power_of_two <= N:
    result.append(power_of_two)
    power_of_two *= 2

print("Целые степени двойки, не превосходящие заданого :", result)