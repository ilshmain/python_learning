# Задание_1
# Задан массив из 10 чисел. Напишите программу, которая выводит их сумму.
# 1) Входные данные: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Выходные данные: 45
# 2) Входные данные: 1, 1, 1, 1, 1, 1, 1, 1, 1, 1. Выходные данные: 10
# 3) Входные данные: 8, 4, 5, 3, 9, 2, 3, 4, 5, 1. Выходные данные: 44

"""
a = input().split(', ')
summa = 0
for i in a:
    summa = summa + int(i)
print(summa)
"""

# Задание_2
# Задан массив из n чисел. Напишите программу, которая считает и выводит количество чисел равных нулю.
# 1) Входные данные: 0, 1, 2, 3, 4. Выходные данные: 1
# 2) Входные данные: 1, 0, 1, 0, 1, 0, 1, 0, 1, 0. Выходные данные: 5
# 3) Входные данные: 8, 4, 0, 3, 9, 2, 3, 0. Выходные данные: 2

"""
a = input().split(', ')
summa = 0
for i in a:
    if int(i) == 0:
        summa += 1
print(summa)
"""

# Задание_3
# По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
# 1) Входные данные: 1
# 2) Входные данные: 3
# 3) Входные данные: 5

"""
a = int(input())
if (a > 9) | (a < 1):
    print('Число не соответсвует условию')
else:
    i = 1
    n = str(i)
    while i <= a:
        print(n)
        i += 1
        n = n + str(i)
"""

# Задание_4
# Дополните код из предыдущего задания, чтобы теперь получалась пирамида.
# То есть каждая ступень состоит из чисел от 1 до i и обратно.
# Примечание: по условию задачи, нельзя использовать функции
# 1) Входные данные: 1
# 2) Входные данные: 3
# 3) Входные данные: 5

"""
a = int(input())
i = 1
q = 0
n = str(i)

if (a > 9) | (a < 1):
    print('Число не соответсвует условию')
if (a % 2 == 0) | (a == 1):
    while i < a:
        print(n)
        i += 1
        n = n + str(i)
else:
    while i <= a:
        k = ''
        p = q
        while p < a - 1:
            k = k + ' '
            p += 1
        k = k + n
        if i != 1:
            z = i - 1
            while z > 0:
                k = k + str(z)
                z -= 1
        p = q
        while p < a - 1:
            k = k + ' '
            p += 1
        i += 1
        q += 1
        n = n + str(i)
        print(k)
"""

# Задание_5
# Дополните код из предыдущего задания, чтобы теперь получался ромб.
# То есть количество ступеней должно равняться числу n*2-1.
# Примечание: по условию задачи, нельзя использовать функции
# 1) Входные данные: 1
# 2) Входные данные: 3
# 3) Входные данные: 5

"""
a = int(input())
i = 1
q = 0
list = []
n = str(i)

if (a > 9) | (a < 1):
    print('Число не соответсвует условию')
if (a % 2 == 0) | (a == 1):
    while i < a:
        print(n)
        i += 1
        n = n + str(i)
else:
    while i <= a:
        k = ''
        p = q
        while p < a - 1:
            k = k + ' '
            p += 1
        k = k + n
        if i != 1:
            z = i - 1
            while z > 0:
                k = k + str(z)
                z -= 1
        p = q
        while p < a - 1:
            k = k + ' '
            p += 1
        i += 1
        q += 1
        n = n + str(i)
        print(k)
        list.append(k)
    m = a - 2
    while a - 1 > 0:
        print(list[m])
        m -= 1
        a -= 1
"""