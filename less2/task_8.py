n=int(input(''))
a=int(input(''))
j=0
for i in range(1,n+1):
    b=int(input())
    while b!=0:
        if b%10==a:
            j+=1
        b//=10
print(j)
