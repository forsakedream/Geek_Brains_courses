# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
import random

n=int(input('Введите длинну массива: '))
a = [random.randint(-100, 100) for _ in range(n)]
print(a)


def bubble(a):
    for i in range(1, len(a)+1):
        for j in range(len(a) - i):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(bubble(a))
print(a)