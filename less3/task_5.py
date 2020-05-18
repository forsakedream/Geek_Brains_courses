# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

n=int(input('Введите длинну массива: '))
a = [random.randint(-100, 100) for _ in range(n)]
print(a)
i = 0
max_i=-1
for item in a:
    if item < 0 and max_i==-1:
        max_i=i
    elif item <0 and item > a[max_i]:
        max_i=i
    i+=1
print(f'Максимальный отрицательный элемент находится на {max_i} позиции и равен {a[max_i]}')
