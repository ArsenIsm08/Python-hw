# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# РРРОРООРОРР -> 4
# ОРОРОРОРОРО -> 5

money = input("Введите строку монеток: ")

count = 0
count2 = 0
for coin in money:
    if coin == "О":
        count += 1
    elif coin == "Р":
        count2 += 1

if count > count2:
    print(f"Нужно перевернуть Р: {count2} штук")
elif count2 > count:
    print(f"Нужно перевернуть O: {count} штук")
elif count == count2:
    print("У вас равное количество монет, переворачивайте любую")
