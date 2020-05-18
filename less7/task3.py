# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

m = int(input('Введите m для 2m+1: '))
a = [random.randint(0, 50) for _ in range(2*m + 1)]
print(a)


def find_median(array):
    if len(array) == 1:
        return array[0]
    elif len(array) > 1:
        b = array.copy()
        i_max, i_min = 0, 0
        for i in range(len(b)):
            if b[i] >= b[i_max]:
                i_max = i
            elif b[i] <= b[i_min]:
                i_min = i
        if i_max < i_min:
            i_min -= 1
        b.pop(i_max)
        b.pop(i_min)
        return find_median(b)


print(find_median(a))
a.sort()
print(a)