n=int(input('Введите количество чисел прогрессии '))
s=1
a=1
for i in range(1,n):
    a=a*(-0.5)
    s+=a
print(s)