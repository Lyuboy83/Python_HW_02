# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# Первый вариант

# a = input('Введите трёзначное число: ')
# sum = (int(a[0]) + int(a[1]) + int(a[2]))
# print('Сумма цифр числа :')
# print(sum)

# n = input("Введите трехзначное число: ")

# Извлекается первый[0] символ строки,
# преобразуется к целому.
# Аналогично второй[1] и третий[2].
# a = int(n[0])
# b = int(n[1])
# c = int(n[2])

# print("Сумма цифр числа:", a + b + c)

# Второй вариант

# n = input("Введите трехзначное число: ")
# n = int(n)
#
# n1 = n % 10
# n = n // 10
# n2 = n % 10
# n = n // 10
#
# print("Сумма цифр числа:", n + n1 + n2)
#
