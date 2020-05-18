# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

n=int(input('Введите длинну массива: '))
a = [random.randint(-100, 100) for _ in range(n)]
print(a)
i=0
min_i=0
max_i=0
max = a[0]
min = a[0]
for item in a:
    if item >= max:
        max=item
        max_i=i
    elif item <= min:
        min=item
        min_i=i
    i+=1
print(f'Минимум: a[{min_i}] = {min}, Максимум: a[{max_i}] = {max}')
if min_i > max_i:
    min_i, max_i = max_i, min_i
s=0
for i in range(min_i+1,max_i):
    s+=a[i]
print(f'Сумма элементов: {s}')