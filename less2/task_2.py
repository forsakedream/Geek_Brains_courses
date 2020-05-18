a= int(input('Введите число: '))
i = 0
j = 0
while a != 0:
    if (a % 10) % 2 == 0:
        i += 1
    else:
        j += 1
    a //= 10
print(f'Нечетные: {j}; четные: {i}')