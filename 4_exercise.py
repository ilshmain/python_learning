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

s = str(input())
i = len(s)

numb_in_str = '1234567890'
spec_symb = '!@#$%^&*()-+'
sum_simb = ''
last_line = ''

s_low = s.islower()
s_high = s.isupper()
if i < 12:
    i = 12 - i
    sum_simb = ('увеличить число символов на ' + str(i) + ', ')
i = len(spec_symb) - 1
while i >= 0:
    if s.find(spec_symb[i]) > 0:
        res_spec_symb = 'True'
        break
    else:
        res_spec_symb = 'False'
    i -= 1
i = len(numb_in_str) - 1
while i >= 0:
    if s.find(numb_in_str[i]) > 0:
        res_numb_in_str = 'True'
        break
    else:
        res_numb_in_str = 'False'
    i -= 1
if (sum_simb != '') | (res_spec_symb == 'False') | (res_numb_in_str == 'False') | (not(s_low)) | (not(s_low)):
    last_line = 'Слабый пароль. Рекомендации: '
if sum_simb != '':
    last_line = last_line + sum_simb
if not(s_low):
    last_line = last_line + 'добавить 1 строчную букву, '
if not (s_high):
    last_line = last_line + 'добавить 1 заглавную букву, '
if res_numb_in_str == 'False':
    last_line = last_line + 'добавить 1 цифру, '
if res_spec_symb == 'False':
    last_line = last_line + 'добавить 1 спецсимвол, '
i = len(last_line) - 2
last_line = last_line[:i] + '.'
print(last_line)
