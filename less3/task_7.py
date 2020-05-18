# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import random

n=int(input('Введите длинну массива: '))
a = [random.randint(-10, 10) for _ in range(n)]
print(a)
min = 0
min2 = 1
if a[1]<a[0]:
    min, min2 = min2, min
for i in range(2, n):
    if a[i] < a[min2]:
        b = min2
        min2=i
        if a[b] < a[min]:
            min = b
    elif a[i] < a[min]:
        min = i
print(f'Первый минимум: {a[min2]}; второй минимум: {a[min]}')

