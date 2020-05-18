def calc(a,b,sign):
    if sign=='+' or sign=='-' or sign=='/' or sign=='*':
        if sign=='+':
            return(a+b)
        elif sign=='-':
            return(a-b)
        elif sign=='*':
            return(a*b)
        elif sign=='/':
            if b!=0:
                return(a/b)
            else:
                return('Делить на ноль нельзя!')
    else:
        return('Неверный знак операции!')
while True:
    a=int(input('Введите число a = '))
    sign=input('Введите знак операции ')
    b = int(input('Введите число b = '))
    if sign !='0':
        print(calc(a,b,sign))
    else:
        break
