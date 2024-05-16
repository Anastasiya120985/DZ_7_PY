# Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
# Bill Gates
def text_print():
    a = '\"Don\'t compare yourself with anyone in this world... \nif you do so, you are insulting yourself.\"'
    b = 'Bill Gates'
    print(f'{a}\n{b:>50}')

text_print()

# Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними

def even_numbers(a, b):
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        if i%2 == 0:
            print(i)

beg = int(input('Введите первое число '))
end = int(input('Введите второе число '))
even_numbers(beg, end)

# Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.

def square(length, simbol, fillings):
    if fillings:
        for i in range(length):
            print(simbol * length)
    else:
        print(simbol * length)
        for i in range(length - 2):
            print(simbol + ' '*(length-2) + simbol)
        print(simbol * length)

l = int(input('Введите длину стороны квадрата '))
s = input('Введите символ ')
f = bool(input('Введите True для отображения заполненого квадрата или False для пустого '))
square(l, s, f)

# Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров.

def min_numbers(num_list):
    minimum = num_list[0]
    for i in num_list:
        if minimum > i:
            minimum = i
    return minimum

number_list = list(map(int, input('Введите через пробел 5 чисел ').split()))
print(f'Минимальное число - {min_numbers(number_list)}')

# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
# передаются в качестве параметров. Если границы диапанижняя граница), их нужно поменять местами.

def multip_range(a, b):
    if a > b:
        a, b = b, a
    mult = 1
    for i in range(a, b+1):
        mult = i * mult
    return mult

a = int(input('Введите начало диапозона '))
b = int(input('Введите конец диапозона '))
print(f'Произведение чисел в диапозоне между {a} и {b} равно {multip_range(a, b)}')

# Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра. Из
# функции нужно вернуть полученное количество цифр. Например, если передали 3456, количество цифр будет 4.

def number_of_digits(num):
    kol = 0
    while num > 0:
        num //= 10
        kol += 1
    return kol

a = int(input('Введите число '))
print(f'Количество цифр в числе {a} равно {number_of_digits(a)}')


# Напишите функцию, которая проверяет является ли число палиндромом. Число передаётся в качестве параметра.
# Если число палиндром нужно вернуть из функции true, иначе false. «Палиндром» — это число, у которого первая часть
# цифр равна второй перевернутой части цифр. Например, 123321—палиндром(первая часть 123, вторая 321, которая
# после переворота становится 123), 546645 — палиндром, а 421987 — не палиндром

def palindrom(text):
    reverse_text = text[::-1]
    if text == reverse_text:
        print(f'{text} - палиндром')
    else:
        print(f'{text} - не является палиндромом')

string = input('Введите строку ')
palindrom(string)



