# Урок 12. Множества

# Задание_1
# Дан список чисел. Напишите программу, которая определяет,
# сколько в нем встречается различных чисел, используя множества.
# 1) Входные данные: 1, 2, 3, 2, 1.
# Выходные значения: 3.
# 2) Входные данные: 1, 2, 3, 4, 5, 6, 7.
# Выходные значения: 7.
# 3) Входные данные: 1, 1, 1, 1, 1.
# Выходные значения: 1.
# 4) Входные данные: 1, 2, 3, 1, 1.
# Выходные значения: 3.

"""
a = input().split(', ')
print(len(set(a)))
"""

# Задание_2
# Даны два списка чисел. Напишите программу, которая определяет,
# сколько в них встречается общих чисел, используя множества.

# 1) Входные данные: 1, 2, 3
# 1, 4, 5.
# Выходные значения: 1.
# 2) Входные данные: 1, 2, 3, 4, 5, 6, 7
# 10, 2, 3, 4, 8.
# Выходные значения: 3.
# 3) Входные данные: 1, 10, 223, 413, 2
# 2, 40, 12, 100, 10.
# Выходные значения: 2.

"""
a = input().split(', ')
b = input().split(', ')

a = set(a)
b = set(b)
c = a.intersection(b)
print(len(c))
"""

# Задание_3
# Даны два множества чисел. Напишите программу, которая определяет, является ли первое множество подмножеством второго.
# Множество является подмножеством другого множества, если все данные первого совпадают с частью данных из второго.
# Если множества совпадают, они не являются подмножествами друг друга.
# 1) Входные данные: 1, 2, 3
# 1, 4, 5.
# Выходные значения: False.
# 2) Входные данные: 1, 2, 3, 4, 5, 6, 7
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.
# Выходные значения: True.
# 3) Входные данные: 1, 10, 223, 413, 2
# 1, 10, 223, 413, 2.
# Выходные значения: False.

"""
a = input().split(', ')
b = input().split(', ')

a = set(a)
b = set(b)
if a == b:
    print(False)
    exit(0)
c = a.intersection(b)
if c == a:
    print(True)
else:
    print(False)
"""