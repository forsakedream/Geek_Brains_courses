#Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).
a = int(input('Введите первое число: a = '))
b = int(input('Введите второе число: b = '))
c = int(input('Введите третье число: c = '))
if (b>a) and (b<c):
    print(f'Среднее число b = {b}')
elif c>a:
    print(f'Среднее число c = {c}')
else:
    print(f'Среднее число a = {a}')