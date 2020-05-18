# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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
        max = item
        max_i = i
    elif item <= min:
        min=item
        min_i=i
    i+=1
a[max_i], a[min_i] = a[min_i], a[max_i]
print(a)