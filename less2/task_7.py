n=int(input('Введите число: '))
s=0
for i in range(1,n+1):
    s+=i
if s==(n*(n+1)/2):
    print('Равенство выполняется!')
print(f'Сумма чисел: {s}')
