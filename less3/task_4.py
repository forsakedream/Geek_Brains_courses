# 4. Определить, какое число в массиве встречается чаще всего.
import random

n=int(input('Введите длинну массива: '))
a = [random.randint(0, 100) for _ in range(n)]
print(a)

d=a[0]
max_freq=1
for i in range(n-1):
    freq = 1
    for k in range(i+1,n):
        if a[i]==a[k]:
            freq+=1
    if freq > max_freq:
        max_freq = freq
        d = a[i]
if max_freq > 1:
    print(f'Чаще всего встречается число {d}. Оно встречается {max_freq} раз(а)')
else:
    print('Все числа уникальны')