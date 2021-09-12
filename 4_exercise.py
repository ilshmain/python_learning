# Задание_1
# Дана строка: Abraсadabra
# Требуется:

"""
str = 'Abraсadabra'
# Вывести третий символ этой строки.
print(str[2])
# Вывести предпоследний символ этой строки.
print(str[len(str) -2])
# Вывести первые пять символов этой строки.
print(str[:5])
# Вывести строку, кроме последних двух символов.
print(str[:len(str) - 2])
# Вывести все символы с четными индексами (считайте, что 0 - четный индекс).
i = 0
while i < len(str):
    if (i == 0) | (i%2 == 0):
        print(str[i])
    i += 1
print(' ')
# Вывести все символы с нечетными индексами.
i = 0
while i < len(str):
    if (i != 0) | (i%2 != 0):
        print(str[i])
    i += 1
print(' ')
# Вывести все символы в обратном порядке.
i = len(str)
while i > 0:
    print(str[i - 1])
    i -= 1
print(' ')
"""

# Задание_2
# Напишите код, который обрабатывает строковые данные и возвращает их с первыми заглавными буквами в каждом слове.
# 1) Входные данные: 'ivan ivanov'
# 2) Входные данные: 'can    you   solve  it?'
# 3) Входные данные: 'abraсadabra'
# 4) Входные данные: 'a1 2b  3   abc d3e r2D2'
"""
s = input().split(' ')
i = len(s)
k = 0
while k < i:
    if s[k] != '':
        per = s[k][0].upper()
        if per.isalpha():
            s[k] = s[k][1:]
            s[k] = per + s[k]
            print(s[k])
        else:
            print(s[k])
    k += 1
"""

# Задание_3
# Пароль считается надежным, если его длина составляет не менее 12 символов,
# при этом он должен содержать хотя бы одну заглавную букву, хотя бы одну строчную букву,
# хотя бы одну цифру и хотя бы один спецсимвол. Напишите код,
# который обрабатывает строковые данные и выводит сообщение о том,
# надежен ли пароль или нет. В случае, если пароль не надежен,
# код должен выдавать рекомендации для усиления надежности пароля.
# 1) Входные данные: 'qwerty'.
#     Выходные данные: 'Слабый пароль. Рекомендации: увеличить число символов - 6, добавить 1 заглавную букву,
#     добавить 1 цифру, добавить 1 спецсимвол '
# 2) Входные данные: 'Qwert_Y'.
#      Выходные данные: 'Ошибка. Запрещенный спецсимвол'
# 3) Входные данные: 'Q123wer123tY'.
#      Выходные данные: 'Слабый пароль. Рекомендации: добавить 1 спецсимвол'
# 4) Входные данные: '@PowerRangers123@'.
#      Выходные данные: 'Сильный пароль.'

s = str(input())

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numb_in_str = '1234567890'
spec_symbol = '!@#$%^&*()-+'

k = 0
i = len(s)
res_spec_symbol = -1
res_numb_in_str = -1
low_symbol = -1
high_symbol = -1
last_line = 'Слабый пароль. Рекомендации: '
all_symbol = ascii_uppercase + ascii_lowercase + numb_in_str + spec_symbol

while k < len(s):
    flag = all_symbol.find(s[k])
    if flag == -1:
        print('Ошибка. Запрещенный спецсимвол')
        exit(0)
    if (i < 12) & (k == 0):
        i = 12 - i
        last_line = last_line + 'увеличить число символов на ' + str(i) + ', '
    if high_symbol == -1:
        high_symbol = ascii_uppercase.find(s[k])
    if low_symbol == -1:
        low_symbol = ascii_lowercase.find(s[k])
    if res_spec_symbol == -1:
        res_spec_symbol = spec_symbol.find(s[k])
    if res_numb_in_str == -1:
        res_numb_in_str = numb_in_str.find(s[k])
    k += 1
if high_symbol == -1:
    last_line = last_line + 'добавить 1 заглавную букву, '
if low_symbol == -1:
    last_line = last_line + 'добавить 1 строчную букву, '
if res_numb_in_str == -1:
    last_line = last_line + 'добавить 1 цифру, '
if res_spec_symbol == -1:
    last_line = last_line + 'добавить 1 спецсимвол, '
if last_line != 'Слабый пароль. Рекомендации: ':
    i = len(last_line) - 2
    last_line = last_line[:i] + '.'
else:
    last_line = 'Сильный пароль.'
print(last_line)
