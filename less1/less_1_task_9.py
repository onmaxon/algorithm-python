# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три числа! ')
n1 = int(input('Первое число: '))
n2 = int(input('Второе число: '))
n3 = int(input('Третье число: '))

if n2 < n1 < n3 or n3 < n1 < n2:
    print('Среднее:', n1)
elif n1 < n2 < n3 or n3 < n2 < n1:
    print('Среднее:', n2)
else:
    print('Среднее:', n3)
