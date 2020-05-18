import sys
# В качестве задачи выбрана задача: В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

# Версия и платформа: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] win32
import random

# 1 вариант
lst = [random.randint(-100, 100) for _ in range(100)]
i = 0
max_i = -1
for item in lst:
    if item < 0 and max_i == -1:
        max_i = i
    elif item < 0 and item > lst[max_i]:
        max_i = i
    i += 1
print(f'Максимально отрицательное число: {lst[max_i]}. Его индекс: {max_i}')

# Количество байт: 1757


# 2 вариант
lst = [random.randint(-100, 100) for _ in range(100)]
lst_set = set(lst)
lst2 = []
max_item = 0
for i in lst_set:
    if i < 0:
        lst2.append(i)

for item in lst2:
    if item > max_item:
        item = max_item
print(f'Максимально отрицательное число: {item}. Его индекс: {lst.index(item)}')



# Количество байт: 10601

# 3 вариант
lst = [random.randint(-100, 100) for _ in range(100)]
lst_set = set(lst)
lst2 = []
for i in lst_set:
    if i < 0:
        lst2.append(i)
max_lst = max(lst2)
index_max = lst.index(max(lst2))
print(f'Максимально отрицательное число: {max_lst}. Его индекс: {index_max}')

# Вычисление количества памяти
s = 0
for item in list(locals().values()):
    s += sys.getsizeof(item)

print(s)

# 10605

# Вывод: наиболее эффективно память используется в первом варианте кода.
# Объяснить такой результат можно использованием всего одного списка и меньшего количества переменных.
