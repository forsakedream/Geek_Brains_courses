a= int(input('Введите число: '))
s=''
while a != 0:
    s=f'{s}{a%10}'
    a //= 10
    s=int(s)
print(s)
