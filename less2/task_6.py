import random
a=random.randint(0, 100)
for j in range(1,11):
    print(f'Попытка №{j}:')
    b=int(input('Что за число? '))
    if b==a:
        print('Вы угадали!')
        break
    elif b<a:
        print('Ваше число меньше')
    elif b>a:
        print('Ваше число больше')
print(f'Загаданное число: {a}')

