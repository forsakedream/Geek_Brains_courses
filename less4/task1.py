import cProfile
# В качестве задачи выбрана задача: В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

# n - длинна массива

def max_otr1(n):
    lst = [random.randint(-100, 100) for _ in range(n)]
    i = 0
    max_i = -1
    for item in lst:
        if item < 0 and max_i == -1:
            max_i = i
        elif item < 0 and item > lst[max_i]:
            max_i = i
        i += 1
    return f'Максимально отрицательное число: {lst[max_i]}. Его индекс: {max_i}'

# 1000 loops, best of 5: 1.26 msec per loop - для длинны 1000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#      1000    0.001    0.000    0.001    0.000 random.py:174(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:218(randint)
#      1000    0.000    0.000    0.001    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.002    0.002 task1.py:10(<listcomp>)
#         1    0.000    0.000    0.002    0.002 task1.py:9(max_otr1)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1258    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
# 1000 loops, best of 5: 12.6 msec per loop - для длинны 10000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.019    0.019 <string>:1(<module>)
#     10000    0.006    0.000    0.013    0.000 random.py:174(randrange)
#     10000    0.002    0.000    0.016    0.000 random.py:218(randint)
#     10000    0.005    0.000    0.007    0.000 random.py:224(_randbelow)
#         1    0.002    0.002    0.018    0.018 task1.py:10(<listcomp>)
#         1    0.001    0.001    0.019    0.019 task1.py:9(max_otr1)
#         1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12800    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

def max_otr2(n):
    lst = [random.randint(-100, 100) for _ in range(n)]
    lst_set = set(lst)
    lst2 = []
    max_item = 0
    for i in lst_set:
        if i < 0:
            lst2.append(i)

    for item in lst2:
        if item > max_item:
            item = max_item
    return f'Максимально отрицательное число: {item}. Его индекс: {lst.index(item)}'

# 1000 loops, best of 5: 1.18 msec per loop - для длинны 1000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#      1000    0.001    0.000    0.001    0.000 random.py:174(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:218(randint)
#      1000    0.000    0.000    0.001    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.002    0.002 task1.py:36(max_otr2)
#         1    0.000    0.000    0.002    0.002 task1.py:37(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1278    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
# 11.6 msec per loop - для длинны 10000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.018    0.018 <string>:1(<module>)
#     10000    0.006    0.000    0.013    0.000 random.py:174(randrange)
#     10000    0.002    0.000    0.015    0.000 random.py:218(randint)
#     10000    0.005    0.000    0.007    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.018    0.018 task1.py:36(max_otr2)
#         1    0.002    0.002    0.018    0.018 task1.py:37(<listcomp>)
#         1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12637    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
def max_otr3(n):
    lst = [random.randint(-100, 100) for _ in range(n)]
    lst_set = set(lst)
    lst2 = []
    for i in lst_set:
        if i < 0:
            lst2.append(i)
    return f'Максимально отрицательное число: {max(lst2)}. Его индекс: {lst.index(max(lst2))}'

# 1000 loops, best of 5: 1.19 msec per loop - для длинны 1000

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#      1000    0.001    0.000    0.002    0.000 random.py:174(randrange)
#      1000    0.000    0.000    0.003    0.000 random.py:218(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.003    0.003 task1.py:81(max_otr3)
#         1    0.000    0.000    0.003    0.003 task1.py:82(<listcomp>)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#        99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1250    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
# 1000 loops, best of 5: 11.6 msec per loop - для длинны 10000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.018    0.018 <string>:1(<module>)
#     10000    0.006    0.000    0.013    0.000 random.py:174(randrange)
#     10000    0.002    0.000    0.015    0.000 random.py:218(randint)
#     10000    0.005    0.000    0.007    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.018    0.018 task1.py:81(max_otr3)
#         1    0.002    0.002    0.018    0.018 task1.py:82(<listcomp>)
#         1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#       100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12728    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
cProfile.run('max_otr1(10000)')

# Вывод: все функции примерно одинаковы. Вторая и третья реализация быстрее, но сложнее. Однако, сложность не оказывается критичной в данной ситуации